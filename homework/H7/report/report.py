def generate_report(data: dict[str, int]) -> str:
    # sorting asscending
    above_80_sorted = sorted([(k, v) for k,v in data.items() if v >= 80], key=lambda x: x[1])
    raports = ["Students with a score above 80", "*******************************"]
    for student in above_80_sorted:
        raport = f"{student[0]} | {student[1]:>5}"
        raports.append(raport)

    return "\n".join(raports)
