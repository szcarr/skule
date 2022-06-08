def foo(ufstring):
    ufstring = list(ufstring)
    for c in range(len(ufstring)):
        if str(ufstring[c]) == "`":
            ufstring[c] = "'"

    fstring = ""
    for i in range(len(ufstring)):
        fstring = fstring + ufstring[i]
    return fstring

fstring = '''INSERT INTO `tegneseriefigurer`.`blad` (`bladnavn`) VALUES ('Donald Duck & Co');
INSERT INTO `tegneseriefigurer`.`blad` (`bladnavn`) VALUES ('Asterix');
INSERT INTO `tegneseriefigurer`.`blad` (`bladnavn`) VALUES ('Batman');
INSERT INTO `tegneseriefigurer`.`blad` (`bladnavn`) VALUES ('Pondus');
INSERT INTO `tegneseriefigurer`.`blad` (`bladnavn`) VALUES ('Nemi');
INSERT INTO `tegneseriefigurer`.`blad` (`bladnavn`) VALUES ('Spiderman');

 

INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Donald Duck', '1934', '1');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Skrue McDuck', '1947', '1');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Langbein', '1932', '1');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Asterix', '1959', '2');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Obelix', '1959', '2');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Idefix', '1959', '2');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Batman', '1939', '3');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Jokeren', '1949', '3');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Pondus', '1995', '4');
INSERT INTO `tegneseriefigurer`.`figur` (`figurnavn`, `aarstall`, `blad_id`) VALUES ('Jokke', '1995', '4');'''

print(foo(fstring))

