import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    ws1 = pd.read_csv("work.csv")
    print(round(np.float64(ws1['Стать']=="male").sum()/(np.float64(ws1['Стать']=="male").sum()+np.float64(ws1['Стать']=="female").sum()),2)*100,"%")
    print("Man ", np.float64(ws1['Стать']=="male").sum())
    print("Woman ", np.float64(ws1['Стать']=="female").sum())
    ws2 = pd.read_excel("Second_work.xlsx")
    child = pd.read_excel("Second_work.xlsx", sheet_name= 1)
    enchild = pd.read_excel("Second_work.xlsx", sheet_name= 2)
    man = pd.read_excel("Second_work.xlsx", sheet_name= 3)
    older =pd.read_excel("Second_work.xlsx", sheet_name= 4)
    agecount = ws2['Вік'].value_counts()
    plt.bar(agecount.index,agecount.values)

    plt.title("Графік")
    plt.xlabel("Вік")
    plt.ylabel("Кількість")

    plt.show()

    def man_or_woman(dava):
        state = []
        x = 0
        i = 0
        for work in dava["По батьковій"]:
            sd = ""
            for rev in work[::-1]:
                if len(sd) < 4:
                    sd = sd + rev
            if (sd == 'анві') | (sd == 'анвї'):
                state.append("woman")
                i = i+1
            else:
                state.append("man")
                x = x+1
        return [i,x]
    sac = man_or_woman(child)
    sae = man_or_woman(enchild)
    sam = man_or_woman(man)
    sao = man_or_woman(older)
    data = {
        "Кількість":["younger_18","18-45","45-70","older_70"],
        "Man":[sac[1],sae[1],sam[1],sao[1]],
        "Woman":[sac[0],sae[0],sam[0],sam[0]]
    }
    df = pd.DataFrame(data)
    df.set_index("Кількість").plot(kind = 'bar', stacked = True)
    plt.title("Графік")
    plt.ylabel("Кількість")
    plt.show()
    print("OK")
except:
    print("Відсутній файл")
