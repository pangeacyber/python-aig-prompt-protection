from __future__ import annotations

import sys

import click
from openai import OpenAI
from pangea import PangeaConfig
from pangea.services import AIGuard


@click.command()
@click.option("--model", default="gpt-4o-mini", show_default=True, required=True, help="OpenAI model.")
@click.option(
    "--ai-guard-token",
    envvar="PANGEA_AI_GUARD_TOKEN",
    required=True,
    help="Pangea AI Guard API token. May also be set via the `PANGEA_AI_GUARD_TOKEN` environment variable.",
)
@click.option(
    "--pangea-domain",
    envvar="PANGEA_DOMAIN",
    default="aws.us.pangea.cloud",
    show_default=True,
    required=True,
    help="Pangea API domain. May also be set via the `PANGEA_DOMAIN` environment variable.",
)
@click.option(
    "--openai-api-key",
    envvar="OPENAI_API_KEY",
    required=True,
    help="OpenAI API key. May also be set via the `OPENAI_API_KEY` environment variable.",
)
@click.argument("prompt")
def main(
    *,
    prompt: str,
    model: str,
    ai_guard_token: str,
    pangea_domain: str,
    openai_api_key: str,
) -> None:
    config = PangeaConfig(domain=pangea_domain)
    ai_guard = AIGuard(token=ai_guard_token, config=config)

    # Guard the prompt before sending it to the LLM.
    guarded = ai_guard.guard_text(prompt)
    assert guarded.result
    redacted_prompt = guarded.result.redacted_prompt or prompt

    # Generate chat completions.
    stream = OpenAI(api_key=openai_api_key).chat.completions.create(
        messages=[{"role": "user", "content": redacted_prompt}], model=model, stream=True
    )
    for chunk in stream:
        for choice in chunk.choices:
            sys.stdout.write(choice.delta.content or "")
            sys.stdout.flush()

        sys.stdout.flush()

    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
