<<<<<<< HEAD
\# Climate Challenge Week 0



\##  Project Setup



This project demonstrates setting up a Python development environment with Git and CI using GitHub Actions.





\##  Prerequisites



Make sure you have the following installed:



\* Python 3.x

\* Git





\##  Clone the Repository



```bash

git clone https://github.com/eyerus-getachew/climate-challenge-week0.git

cd climate-challenge-week0

```





\##  Create Virtual Environment



```bash

python -m venv venv

```





\##  Activate Virtual Environment



\### Windows (PowerShell)



```bash

venv\\Scripts\\Activate.ps1

```



\### macOS / Linux



```bash

source venv/bin/activate

```





\##  Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\##  Continuous Integration



This project uses GitHub Actions for CI.



On every push to the `main` branch, the workflow:



\* Installs dependencies

\* Checks Python version





\##  Project Structure



```

├── src/

├── notebooks/

├── tests/

├── scripts/

├── .github/workflows/

├── requirements.txt

├── README.md

```



\---



\##  Status



Setup completed successfully with:



\* Virtual environment configured

\* Dependencies tracked

\* CI workflow added



