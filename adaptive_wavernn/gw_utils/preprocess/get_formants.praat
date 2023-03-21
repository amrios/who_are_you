
############################################################
###    get_formants.praat
###
###
###    MEASURES FORMANT VALUES FOR SEGMENTS IN A TEXTGRID
############################################################

#PROMT THE USER FOR INPUT
form Measure formant values for segments in a textgrid
    sentence sound_file myname
    positive maximum_formant 5500
    positive number_of_formants 5
endform

#DELETE THE OLD FORMANT FILE IF IT EXISTS
filedelete formants_'sound_file$'.txt

#SELECT THE SOUND AND FIND THE FORMANTS
select Sound 'sound_file$'
To Formant (burg)... 0 'number_of_formants' 'maximum_formant' 0.025 50

#COUNT THE NUMBER OF INTERVALS IN THE PHONES TIER OF THE TEXTGRID
select TextGrid 'sound_file$'
intervals = Get number of intervals... 1

#GO THROUGH THE PHONE INTERVALS ONE BY ONE
for i from 2 to intervals-1
    select TextGrid 'sound_file$'
    phone$ = Get label of interval... 1 i

    #SEE IF THE INTERVAL LABEL IS A PHONE
    if phone$ != "" and phone$ != "sp"

        #GET TIMES DURING THE PHONE
        start = Get starting point... 1 i
        end = Get end point... 1 i
        quarter = start + (end-start) / 4
        halfway = start + (end-start) / 2
        three_quarters = start + (end-start) * 3 / 4

        #IDENTIFY THE WORD
        j = Get interval at time... 2 halfway
        word$ = Get label of interval... 2 j

        word_start = Get starting point... 2 j
        word_end = Get end point... 2 j

        #IDENTIFY THE PRECEDING PHONE
        if start = word_start
            left$ = "#"
        else
            left$ = Get label of interval... 1 i-1
        endif
        
        #IDENTIFY THE FOLLOWING PHONE
        if end = word_end
            right$ = "#"
        else
            right$ = Get label of interval... 1 i+1
        endif
        
        #MEASURE F1 AND F2 AT THREE TIMES
        select Formant 'sound_file$'
        f1_1 = Get value at time... 1 'quarter' Hertz Linear
        f2_1 = Get value at time... 2 'quarter' Hertz Linear
        f1_2 = Get value at time... 1 'halfway' Hertz Linear
        f2_2 = Get value at time... 2 'halfway' Hertz Linear
        f1_3 = Get value at time... 1 'three_quarters' Hertz Linear
        f2_3 = Get value at time... 2 'three_quarters' Hertz Linear

        #RECORD THE FORMANT MEASUREMENTS
        fileappend formants_'sound_file$'.txt 'word$','left$','phone$','right$','f1_1','f2_1','f1_2','f2_2','f1_3','f2_3''newline$'
    endif
endfor
    
select Formant 'sound_file$'
Remove
