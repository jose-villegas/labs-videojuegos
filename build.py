import os

with open("base", "r") as baseMain:
    compileString = baseMain.read()

for i in range (1, 17):
    # Remplace with the correct week report.tex
    weekCompileString = compileString.replace("%%SELECTED_WEEK%%", "semana%d" % i)
    # Creating temporal compilation source file
    tempCompileFile = open("base.tex", "w")
    tempCompileFile.write(weekCompileString)
    tempCompileFile.close()
    # Compile with pdflatex->bibtex->pdflatex->pdflatex
    os.system("pdflatex base.tex -job-name=%s" % "semana%d" % i)
    os.system("bibtex semana%d" % i)
    os.system("pdflatex base.tex -job-name=%s" % "semana%d" % i)
    os.system("pdflatex base.tex -job-name=%s" % "semana%d" % i)

os.remove("base.tex")
os.system("pause")