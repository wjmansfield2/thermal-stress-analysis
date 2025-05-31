import matplotlib.pyplot as plt

def main():

    delta_T = []
    for i in range(50, 120, 2):
        delta_T.append(i)
    
    # Inconel 690
    in690 = {"name":"Inconel 690", "E":200e9, "alpha":13.3 * 10**(-6), "yield strength":200e6}
    # SS304
    ss304 = {"name":"SS304", "E":193e9, "alpha":17.6*10**(-6), "yield strength":150e6}
    # p91
    p91 = {"name":"P91 Steel","E":210e9, "alpha":11.0*10**(-6), "yield strength":300e6}

    materials = [in690, ss304, p91]

    strain_results = []
    strain_results = strain_calc(delta_T, materials)

    stress_results = []
    stress_results = stress_calc(delta_T, materials)

    grapher(delta_T, materials, strain_results, stress_results)

# calculates strain results by material and returns lists of results
def strain_calc(delta_T=[], materials=[]):
    results=[]
    for mat in materials:
        strain_vals = []
        for temp in delta_T:
            strain_vals.append(mat["alpha"]*temp)
        results.append(strain_vals)
    return results

def stress_calc(delta_T=[], materials=[]):
    results=[]
    for mat in materials:
        stress_vals = []
        for temp in delta_T:
            stress_vals.append(mat["E"]*mat["alpha"]*temp)
        results.append(stress_vals) 
    return results

def grapher(temps=[], materials=[], strains = [], stresses=[]):
    # graphs strain values by material
    plt.figure()
    for i in range(0, len(materials)):
        plt.plot(temps, strains[i], label=materials[i]["name"])

    # graph formatting
    plt.xlabel("ΔT (°C)")
    plt.ylabel("Thermal Strain (Unitless)")
    plt.title("Thermal Strain vs. Temperature Gradient in Various Materials")
    plt.legend()
    plt.grid(True)
    plt.savefig("strain_graph.pdf")

    # graphs stress values
    plt.figure()
    for i in range(0, len(materials)):
        mat = materials[i]
        line, = plt.plot(temps, [s / 1e6 for s in stresses[i]], label=mat["name"])
        plt.axhline(
            (mat["yield strength"]) / 1e6,
            color=line.get_color(),
            linestyle="--",
            linewidth=1.5,
            )

    # values hard coded for precision placement    
    plt.text(100, 180, f"{materials[0]['name']} Yield", fontsize=8, style='italic')
    plt.text(100, 133, f"{materials[1]['name']} Yield", fontsize=8, style='italic')
    plt.text(54, 310, f"{materials[2]['name']} Yield", fontsize=8, style='italic')

    # graph formatting    
    plt.xlabel("ΔT (°C)")
    plt.ylabel("Thermal Stress (MPa)")
    plt.title("Thermal Stress vs. Temperature Gradient in Various Materials")
    plt.legend()
    plt.grid(True)
    plt.savefig("stress_graph.pdf")

    plt.show()

if __name__ == "__main__":
    main()