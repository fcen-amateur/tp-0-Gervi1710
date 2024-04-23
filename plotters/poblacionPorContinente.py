import seaborn.objects as so
from gapminder import gapminder

PopContinent=gapminder.groupby(["continent","year"])["pop"].sum()
PopContinentDF=pd.DataFrame(PopContinent)

def plot():
    figura = (
                so.Plot(data=PopContinentDF, x="year", y="pop", color="continent")
                .add(so.Line())
                .label(title="Evolución de la población por continente", x="Año", y="Población (escala logarítmica)")
                .scale(y="log")
        )
    )
    return dict(
        descripcion="Un sofisticado gráfico con el número de países en cada continente",
        autor="La cátedra",
        figura=figura,
    )
