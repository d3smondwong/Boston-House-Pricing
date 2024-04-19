# Boston-House-Pricing
End to end implementation of Boston House Price prediction model

# Software and Tools requirements
1. [Github Account] (https://github.com/)
2. [HerokuAccount] (https://www.heroku.com/)
3. [VSCodeIDE] (https://code.visualstudio.com/)
4. [GitCLI] (https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment
```
conda create -p venv python==3.11 -y
```

See Requirements.txt for packages that are required for installation
```
pip install -r Requirements.txt
```

Example of json to test
```
{
    "data":{
        "crim":0.00632,
        "ZN":18.0,
        "INDUS":2.31,
        "CHAS":0.0,
        "NOX":0.538,
        "RM":6.575,
        "AGE":65.2,
        "DIS":4.09,
        "RAD":1.0,
        "TAX":296,
        "PTRATIO":15.3,
        "B":396.90,
        "LSTAT":4.98        
    }
}
```