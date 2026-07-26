def text_clean(raw_text):
    text=raw_text.replace("\t"," ")
    text=text.replace("\r\n","\n")
    text=text.replace("\r","\n")
    lines=text.split("\n")
    updated_lines=[]
    previous_blank=True
    for line in lines:
        line=line.strip()
        line=" ".join(line.split())
        if line=="":
            if previous_blank:
                continue
            previous_blank=True
        else:
            previous_blank=False
        updated_lines.append(line)
    cleansed_text="\n".join(updated_lines)
    return cleansed_text