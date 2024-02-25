Problem 1:

1st Normal form:
Customer: P(CNum), CName
Property: Composite(PNum, F(CNum), RStart), Paddr, Rent, Onum, Oname, REnd

2nd Normal Form:
Customer: P(CName), CNum
Property: P(PNum), PAddr, OName, ONum
Rent: Composite(CNum, PNum), Rent, RStart, RFinish

3rd Normal Form:
Customer: P(CNum), CName 
Property: P(PNum), PAddr, F(ONum)
Rent: Composite(F(CNum), F(PNum)), Rent, RStart, RFinish
Owner: P(ONum), OName

Problem 2:

1st Normal Form:
Employee: Composite(P(ENum), F(Project)), EName, Job, chg/hr, Hours_Billed
Project: P(PNum), PName, F(PLead)

2nd Normal Form:
Employee: P(ENum), EName, Job, CHG/HR
Project: P(PNum), PName, F(PLead)
WorkTime: Composite(F(ENum), F(PNum)), Hours_Billed

3rd Normal Form:
Employee: P(ENum), EName, F(JName)
Project: P(PNum), PName, F(PLead)
WorkTime: Composite(F(ENum), F(PNum)), Hours_Billed
Job: P(JName), CHG/HR