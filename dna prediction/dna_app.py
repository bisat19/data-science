import pandas as pd
import streamlit as st
import altair as alt
from PIL  import Image

#image = 

#st.image(image, use_column_width=True)

st.write("""
    # DNA Prediction Web App

    This app counts the nucleotide composite of query DNA, 
         and based on the count of nucleotide in the sequence of DNA this 
         web will predict about the DNA!
    ***
    """
)

st.header('Enter DNA Sequence')

sequence_input = "> DNA Query: \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=125)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
#st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

#X

### 2. Print text
st.subheader('Total Nucleotide')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('Nucleotide Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('Nucleotide Bar-chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

### 5. Count GC and AT
#st.subheader('Count GC and AT')
GC = (X['G'])+(X['C'])
AT = (X['A'])+(X['T'])
#st.write('There are  ' + str(GC))
#st.write('There are  ' + str(AT))
st.write("***")
### 6. Estimation of DNA thermal stability
st.subheader('Estimation of DNA Thermal Stability')
if GC > AT:
  st.write("""DNA chains with a high GC content tend to be more thermally 
           stable than those with a high AT content. This means that DNA 
           with a higher GC ratio requires more energy (temperature) to melt 
           (denature) compared to AT-dominant DNA.""")
elif AT > GC:
  st.write("""DNA chains with a high AT content are generally 
           less thermally stable than DNA with a high GC content. 
           This is because the fewer hydrogen bonds in the A-T pair compared to 
           the G-C pair make it easier for the DNA chains to separate or denature at lower 
           temperatures. As a result, DNA with a high AT content requires a lower temperature 
           to denature.""")
else:
  st.write("""With a balanced AT and GC ratio, the thermal stability of DNA will be at the 
           midpoint. This DNA will have moderate stability, because the hydrogen bonds 
           between A-T (two bonds) and G-C (three bonds) are balanced. This means that 
           this DNA will not be as stable at high temperatures as DNA with a high GC content, 
           but it will also not be as easily denatured at low temperatures as DNA with a high AT 
           content.""")
### 7. Genetics Function
st.subheader("Genetics Function")
if GC > AT:
  st.write("""DNA with a high GC content is often found in promoter regions or 
           areas that play an important role in genetic regulation. This could 
           mean that DNA regions with high GC content tend to have different genetic activity, 
           such as being more active in transcription, compared to AT-rich regions.""")
elif AT > GC:
  st.write("""DNA with a high AT content is often found in regions that may have a specific role 
           in genetic processes, such as in the opening of the DNA helix during transcription or 
           replication. High AT content can make DNA easier to unfold, which can influence genetic 
           regulation and transcriptional activity. AT-rich regions may also be associated with TATA 
           box-like elements in gene promoters, which are important for transcription initiation.""")
else:
  st.write("""DNA with a balanced AT and GC ratio can have uniform genetic activity 
           and flexible. There is no clear trend as to whether this DNA is easier to open or not 
           more stable in its helical structure. This allows DNA to maintain structure 
           which is stable while still providing the flexibility required for various processes 
           genetics, such as transcription and replication. For example, a gene promoter can have 
           balance between AT and GC elements, allowing efficient transcriptional regulation.""")

### 8. Evolutionary Interpretation
st.subheader("Evolutionary Interpretation")
if GC > AT:
  st.write("""Organisms that live in extreme environments (e.g. high temperatures) often have DNA 
           with high GC content. In other words, if this data comes from the genome of an organism, 
           it is possible that the organism may have come from an environment that demands greater 
           thermal stability..""")
elif AT > GC:
  st.write("""Organisms with AT-rich DNA content may be more commonly found in environments with more 
           thermally stable conditions, where high thermal stability is not a critical requirement. 
           Additionally, higher AT content could be associated with genetic evolution that emphasizes 
           flexibility or specificity in certain genetic functions. These organisms may not require high 
           DNA thermal stability and may have adapted to environments where speed or ease of 
           transcription takes precedence over DNA structural stability.""")
else:
  st.write("""Organisms with balanced AT and GC DNA content may have adapted to environments that require 
           a balance between structural stability and genetic flexibility. These environments may be less 
           extreme, allowing a balance between the DNA's thermal stability and its ability to adapt to specific genetic needs. 
           From an evolutionary point of view, this balance may provide an advantage in a variety of environmental 
           conditions, making it more flexible in the face of change.""")
  
### 9. Variability and Mutation
st.subheader("Variability and Mutation")
if AT == GC:
  st.write("""DNA with a balanced AT and GC content may have a relatively stable mutation rate, 
           without a clear predisposition toward a particular type of mutation. However, 
           this balance does not rule out the possibility of mutations, such as transitions and 
           transversions, which can still occur but do not show a significant preference for specific 
           changes between AT or GC base pairs.""")
else:
  st.write("""An imbalance between the amounts of A and T and G and C can also indicate a mutation or 
           damage to the DNA. Mutations such as transitions and transversions can change the correct 
           base pairing.""")
  
### 10. DNA Type Analysis
st.subheader("DNA Type Analysis")
if AT == GC:
  st.write("""DNA that has a balance between AT and GC is most likely standard DNA, such as nuclear DNA,
            which obeys classical base pairing rules. However, this balance does not rule out the 
           possibility that the DNA comes from more specific sources, such as mitochondrial DNA or 
           viruses, if found in certain contexts. This DNA may exhibit similar characteristics to 
           standard DNA but may have unique functions and regulations.""")
else:
  st.write("""DNA that does not follow classical base pairing rules (the same A-T and G-C) 
           can come from non-standard forms of DNA, such as DNA in mitochondria, viruses, 
           or DNA fragments that undergo recombination or damage.""")