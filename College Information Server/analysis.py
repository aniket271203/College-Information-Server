
import colours
import subprocess as sp
from datetime import datetime
from conandexec import execute
from conandexec import closeconnection



def a():
    studentExam= input("Enter Exam: ")
    studentMarks= input("Enter Marks: ")
    query = f"""
    SELECT Programs.ProgramName, Colleges.CollegeName
    FROM CollegeAdmitStudents
    JOIN Programs ON CollegeAdmitStudents.ProgramID = Programs.ProgramID
    JOIN Colleges ON CollegeAdmitStudents.CollegeID = Colleges.CollegeID
    WHERE CollegeAdmitStudents.ExamName = "{studentExam}"
    AND {studentMarks} > CollegeAdmitStudents.CutoffScore;
    """
    execute(query)

def b():
    org= input("Organisation : ")
    query=f""" 
    SELECT CollegeName, PercentageOfPlacements
    FROM Colleges
    WHERE CollegeID = (
    SELECT CollegeID
    FROM CollegeListedInRanking
    WHERE RankingOrganization = "{org}"
    ORDER BY RankingValue 
    LIMIT 1
    );
    """
    execute(query)

def c():
    query="""
    SELECT DISTINCT IndustryField
    FROM Startups JOIN Colleges ON Startups.CollegeID = Colleges.CollegeID
    WHERE Colleges.City = 'Mumbai';
    """
    execute(query)


def analysis():
    while(1):
        tmp = sp.call('clear', shell=True)
        print("Choose an operation:")
        print(f"{colours.bcolors.OKCYAN}")
        print("1. Find a list of branches you are eligible for based on a score in an exam")
        print("2. Percentage of placements in the college with the highest ranking by given organisation")
        print("3. Industries in which startups founded in Mumbai Colleges are working")
        print(f"{colours.bcolors.ENDC}{colours.bcolors.WARNING}")
        print("4. Back")
        print("5. Exit")
        print(f"{colours.bcolors.ENDC}")

        ch = input("Enter choice: ").lower()
        tmp = sp.call('clear', shell=True)

        if ch == '1':
            a()
        elif ch == '2':
            b()
        elif ch == '3':
            c()
        elif ch == '4' or ch == 'back':
            return
        elif ch == '5' or ch == 'exit':
            closeconnection()
        else:
            print(f"{colours.bcolors.RED}Invalid Option{colours.bcolors.ENDC}")

        input("Enter any key to continue: ")
