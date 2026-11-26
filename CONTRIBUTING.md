# Contributing to RAGE Intelligence MCP

First of all, thank you for wanting to contribute!

RAGE Intelligence MCP is an independent, open-source research project focused on publicly documented Rockstar Advanced Game Engine (RAGE) technology.

Our mission is to make research more accessible, organised, transparent and useful to everyone.

**You do not need to be an experienced programmer to contribute.**

Research, documentation, source checking, testing and fresh ideas are all valuable contributions.

## 1. Who can contribute?

Everyone is welcome.

You might be:
- A software developer.
- A technical researcher.
- A GTA or RAGE technology enthusiast.
- Someone interested in game engine architecture.
- A beginner learning Python or MCP.
- Someone who simply wants to help improve documentation.

There is a place for different skills and experience levels.

## 2. Ways to contribute

### Research
Help identify publicly available information about RAGE technology.

Examples:
- Developer interviews.
- Technical presentations.
- Public conference talks.
- Official documentation.
- Published technical articles.
- Publicly available game credits.

### Evidence checking
Help review existing research claims.

Ask:
- Is the source reliable?
- Does the source actually support the claim?
- Is the claim worded accurately?
- Are limitations clearly explained?
- Is the information historical or specific to a particular game?

### Documentation
Help make the project easier to understand.

Examples:
- Improve the beginner's guide.
- Explain technical terminology.
- Improve installation instructions.
- Write subsystem documentation.
- Help new contributors get started.

### Development
If you have programming experience, you can help with:
- Python improvements.
- MCP tool development.
- Automated testing.
- Knowledge validation.
- Search functionality.
- Documentation tooling.

### Testing
You can help by:
- Installing the project.
- Testing the MCP connection.
- Running existing tools.
- Reporting bugs.
- Suggesting improvements.

## 3. Adding research claims

Research claims are an important part of this project.

Before suggesting a new claim:

1. Find a publicly accessible source.
2. Read the original material where possible.
3. Identify exactly what the source supports.
4. Avoid making claims stronger than the evidence allows.
5. Record relevant limitations.
6. Reference the source in the source register.
7. Check the existing claim schema before creating a new JSON record.

Use existing records in `knowledge/claims/` as examples.

The project uses evidence-aware research rather than treating every reported statement as established fact.

## 4. Evidence and research standards

We distinguish between:

- **Verified:** Supported by sufficiently strong evidence for the stated scope.
- **Reported:** Described by a source but not independently established.
- **Inference:** A reasoned interpretation based on available evidence.
- **Hypothesis:** A possibility that requires further investigation.
- **Unknown:** Something for which sufficient information is not currently available.

Do not present speculation as fact.

A historical statement about RAGE technology does not automatically establish how GTA VI implements that technology.

Always preserve the scope and limitations of a claim.

## 5. Research safety and project boundaries

RAGE Intelligence is an independent public-source research project.

Contributions must respect the following principles:

- Use lawful, publicly available information.
- Respect intellectual property and privacy.
- Do not submit leaked or private Rockstar source code.
- Do not attempt DRM or anti-cheat bypasses.
- Do not submit stolen credentials or private information.
- Do not encourage unauthorised access to systems.
- Clearly distinguish confirmed information from speculation.

We want to understand technology responsibly.

## 6. How to submit a contribution

If you are new to GitHub, start by reading `README-BEGINNERS.md`.

For a contribution:

1. Find something you would like to improve.
2. Check whether someone is already working on it.
3. Create a GitHub issue describing your idea or proposed change.
4. Fork the repository.
5. Make your changes.
6. Run the relevant tests.
7. Submit a pull request explaining what you changed and why.

Small contributions are welcome.

You do not need to change large amounts of code to make a difference.

## 7. Testing before submitting

From the project directory, run:

```powershell
python -m pip install -e .
```

Validate the knowledge base:

```powershell
rage-knowledge validate
```

Run the automated tests:

```powershell
python -m unittest discover -s tests -v
```

Please include any relevant errors in your pull request.

## 8. Our community principles

We want this project to be:

- Welcoming to beginners.
- Respectful of different experience levels.
- Evidence-driven.
- Technically responsible.
- Transparent about uncertainty.
- Open to constructive criticism.
- Collaborative rather than competitive.

Please be patient with people who are learning.

Nobody starts out knowing everything.

## 9. A good first contribution

Not sure where to begin?

Here are some ideas:

- Find a publicly available RAGE developer interview.
- Check an existing research source.
- Improve one paragraph in the documentation.
- Test the installation instructions.
- Report a problem with the beginner's guide.
- Suggest a new research question.
- Help explain a technical term.

These contributions are genuinely useful.

## 10. Thank you

Every contribution helps make RAGE Intelligence better.

Whether you contribute code, research, documentation, testing or ideas, we appreciate your time.

Our goal is to build something that people can learn from, use and improve together.

**You don't have to be an expert to make a meaningful contribution.**

Welcome to RAGE Intelligence MCP.
