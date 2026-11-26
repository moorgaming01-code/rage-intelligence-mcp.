# RAGE Intelligence MCP
## Beginner's Guide — Get Started

Welcome to RAGE Intelligence MCP!

This guide is for everyone, including people who have never used Python, GitHub or an MCP server before.

The aim of this project is to build an open-source, evidence-aware research tool for exploring publicly documented Rockstar Advanced Game Engine (RAGE) technology.

You do not need to be an expert to get involved. Follow the steps below and you'll be up and running.

---

## 1. What is RAGE Intelligence MCP?

RAGE Intelligence MCP is an open-source research project that makes structured RAGE technology knowledge available to AI assistants through the Model Context Protocol (MCP).

In simple terms, it allows a compatible AI application to access our research tools and knowledge base.

The current server includes four tools:

| Tool | What it does |
|---|---|
| `list_claims` | Lists all research claims in the knowledge base. |
| `search_claims` | Searches research claims using keywords. |
| `get_claim` | Retrieves a specific claim using its ID. |
| `validate_knowledge` | Checks claim records and their source references. |

The project is still developing. These tools provide access to documented research; they do not reveal private Rockstar technology or prove unverified claims.

---

## 2. What do I need?

Before starting, you need:

- A Windows, macOS or Linux computer.
- Python 3.10 or newer.
- An internet connection for installation.
- A compatible MCP client or application.
- A copy of this repository.

You do not need to know how to write Python code to follow this guide.

### Installing Python

If you do not already have Python installed, visit:

https://www.python.org/downloads/

Download and install a suitable version.

On Windows, make sure Python is available from your terminal.

To check your installation, open PowerShell and enter:

```powershell
python --version
```

You should see your installed Python version.

---

## 3. Download the project

Visit the official repository:

https://github.com/moorgaming01-code/newmpc

Select the green **Code** button, then choose **Download ZIP**.

Once downloaded:

1. Find the ZIP file.
2. Extract it.
3. Move the extracted `newmpc` folder somewhere easy to find.

For example:

```text
C:\Users\YourName\Desktop\newmpc
```

You now have a local copy of RAGE Intelligence MCP.

---

## 4. Open PowerShell in the project folder

On Windows:

1. Open the extracted `newmpc` folder.
2. Click the address bar in File Explorer.
3. Type `powershell`.
4. Press Enter.

PowerShell should open inside your project folder.

You should see something similar to:

```powershell
PS C:\Users\YourName\Desktop\newmpc>
```

If you are somewhere else, enter:

```powershell
cd "$HOME\Desktop\newmpc"
```

Adjust the folder path if you saved the project somewhere different.

---

## 5. Install the project

Copy and run:

```powershell
python -m pip install -e .
```

This installs the project and its required Python dependencies.

Wait for the installation to finish.

If it completes successfully, you're ready for the next step.

---

## 6. Check that everything works

We recommend running the checks before connecting the MCP server.

### Validate the knowledge base

```powershell
rage-knowledge validate
```

A successful result should report that the discovered claim records match the schema and source register.

### List the available claims

```powershell
rage-knowledge list
```

### Search the knowledge base

```powershell
rage-knowledge search streaming
```

### Run the automated tests

```powershell
python -m unittest discover -s tests -v
```

If the tests finish with `OK`, the current automated test suite has passed.

---

## 7. Connect RAGE Intelligence to an MCP client

Now for the exciting part!

RAGE Intelligence runs as a local MCP server using standard input/output (STDIO).

This means your MCP-compatible application launches the Python server on your computer and communicates with it directly.

In your MCP client's server configuration, add a new server.

Use these settings:

**Server ID**

```text
rage-intelligence
```

**Transport**

```text
stdio
```

**Command**

Use the full path to your Python executable.

For example:

```text
C:\Users\YourName\AppData\Local\Programs\Python\Python314\python.exe
```

Your Python installation path may be different.

To find yours, run this in PowerShell:

```powershell
python -c "import sys; print(sys.executable)"
```

Copy the result into the Command field.

**Arguments**

Enter one argument per line:

```text
-m
rage_intelligence.server
```

**Working directory**

Enter the full path to your extracted project folder.

For example:

```text
C:\Users\YourName\Desktop\newmpc
```

Leave the Environment field empty unless your MCP client requires something specific.

Save the configuration and enable the server.

---

## 8. Check that the connection works

Your MCP client should show the RAGE Intelligence server as connected.

You should be able to discover four tools:

- `list_claims`
- `search_claims`
- `get_claim`
- `validate_knowledge`

Try running `list_claims`.

You should receive the research claims currently stored in the knowledge base.

You can also try:

```text
Search the RAGE Intelligence knowledge base for streaming.
```

The assistant should be able to use the `search_claims` tool to retrieve matching records.

Congratulations — your MCP server is running!

---

## 9. Understanding the research

One important part of this project is understanding the difference between evidence and speculation.

Research records may include:

- Reported information.
- Verified information.
- Inferences.
- Hypotheses.
- Open questions.
- Unknowns.

A claim appearing in the knowledge base does not automatically mean it has been independently verified.

Always review the original sources and the limitations attached to each claim.

We want this project to be useful, transparent and trustworthy.

---

## 10. Something isn't working?

Don't worry. Most installation problems are straightforward to fix.

### Python is not recognised

Try:

```powershell
python --version
```

If Windows cannot find Python, check that it is installed and available on your system PATH.

### The project cannot be imported

Make sure PowerShell is inside the project folder and run:

```powershell
python -m pip install -e .
```

### The MCP server will not connect

Check these settings:

1. The Command field points to the correct Python executable.
2. The Arguments are entered on separate lines.
3. The Working directory points to the extracted project folder.
4. The project dependencies have been installed.
5. The server can be imported successfully.

You can test the import with:

```powershell
python -c "from rage_intelligence.server import mcp; print('MCP server imported successfully')"
```

If you still have problems, share the error message when asking for help. Please remove any personal information from logs before posting them publicly.

---

## 11. How can I contribute?

Everyone is welcome to help improve RAGE Intelligence MCP.

You could contribute by:

- Finding reliable public research sources.
- Improving existing research records.
- Checking claims against original sources.
- Documenting RAGE technology.
- Improving the Python tools.
- Reporting bugs.
- Improving this beginner's guide.
- Suggesting new MCP tools.

You do not need to be a programmer to make a useful contribution.

Good research, careful source checking and clear documentation are just as important as code.

Please follow the project's safety principles:

- Use publicly available information.
- Respect intellectual property and privacy.
- Do not use leaked or private Rockstar code.
- Do not attempt to bypass DRM or anti-cheat systems.
- Clearly distinguish evidence from inference and speculation.

---

## 12. The project

**Repository:**  
https://github.com/moorgaming01-code/newmpc

RAGE Intelligence MCP is an independent, open-source community research project. It is not affiliated with or endorsed by Rockstar Games or Take-Two Interactive.

Our goal is simple:

Make publicly documented RAGE technology research easier to access, understand, investigate and contribute to.

**You don't have to be an expert to help build something worthwhile.**

Welcome to RAGE Intelligence.
