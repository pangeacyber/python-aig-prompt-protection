# AI Guard Prompt Protection in Python

An example Python app that demonstrates how to use Pangea's [AI Guard][] service
to capture and filter what users are sending to LLMs.

## Prerequisites

- Python v3.12 or greater.
- pip v24.2 or [uv][] v0.4.29.
- A [Pangea account][Pangea signup] with AI Guard enabled.
- An [OpenAI API key][OpenAI API keys].

## Setup

```shell
git clone https://github.com/pangeacyber/python-aig-prompt-protection.git
cd python-aig-prompt-protection
```

If using pip:

```shell
python -m venv .venv
source .venv/bin/activate
pip install .
```

Or, if using uv:

```shell
uv sync
source .venv/bin/activate
```

Then the app can be executed with:

```shell
python aig_prompt_protection.py "My credit card number is 4242 4242 4242 4242."
```

## Usage

```
Usage: aig_prompt_protection.py [OPTIONS] PROMPT

Options:
  --model TEXT           OpenAI model.  [default: gpt-4o-mini; required]
  --ai-guard-token TEXT  Pangea AI Guard API token. May also be set via the
                         `PANGEA_AI_GUARD_TOKEN` environment variable.
                         [required]
  --pangea-domain TEXT   Pangea API domain. May also be set via the
                         `PANGEA_DOMAIN` environment variable.  [default:
                         aws.us.pangea.cloud; required]
  --openai-api-key TEXT  OpenAI API key. May also be set via the
                         `OPENAI_API_KEY` environment variable.  [required]
  --help                 Show this message and exit.
```

## Example

By default, the User Input Prompt recipe will redact credit card numbers. So a
prompt like this:

```shell
python aig_prompt_protection.py "My credit card number is 4242 4242 4242 4242."
```

Will result in "My credit card number is \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*."
being sent to the LLM instead.

[AI Guard]: https://pangea.cloud/docs/ai-guard/
[Pangea signup]: https://pangea.cloud/signup
[OpenAI API keys]: https://platform.openai.com/api-keys
[uv]: https://docs.astral.sh/uv/
