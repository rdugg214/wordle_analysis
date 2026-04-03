import streamlit as st
import pandas as pd
import numpy as np

from wordleanalysis.wordle_game import Wordle

st.title('Wordle')

# https://github.com/ccrsxx/pywebapp/blob/main/app.py

wordle_game = Wordle(words_csv_path="datasets/words.txt")
wordle_game.create_new_game()
pressed = st.button("Start New Game")

guess_word = ""
if pressed:
    wordle_game.create_new_game()

    guess_word = st.text_input("Next guess")

if guess_word != "":
    guess_results = wordle_game.make_guess(guess_word)

    st.write(f"You guessed {guess_word} and your results were {guess_results}")


# st.html("""
# <style>
# th,
# td {
#     border: 2px solid #D3D6DA;
#     font-size: 30px;
#     width: 50px;
#     height: 50px;
#     text-align: center;
#     color: black;
#     font-family: 'Arial';
#     font-weight: bold;
# }

# td.correct {
#     background-color: #79A86B;
#     border-color: #79A86B;
#     color: white;
# }

# td.partially_correct {
#     background-color: #C5B565;
#     border-color: #C5B565;
#     color: white;
# }

# td.incorrect {
#     background-color: #797C7E;
#     border-color: #797C7E;
#     color: white;
# }

# div.wordle_game {
#     width: 1000px;
#     margin: auto;
# }

# table.wordle_grid {
#     border-spacing: 5px;
#     margin: auto;
# }

# div.header_bar {
#     width: 100%;
#     /* border: 2px solid #D3D6DA; */
#     border: #797C7E;
#     border-style: solid;
#     border-bottom: 10px;
#     border-color: #D3D6DA;
#     text-align: center;
# }
# </style>
# <div class="wordle_container">
#     <div class="wordle_game">
#         <table class="wordle_grid">
#             <tr>
#                 <td class="correct">Q</td>
#                 <td class="partially_correct">U</td>
#                 <td class="incorrect">I</td>
#                 <td class="incorrect">C</td>
#                 <td class="incorrect">K</td>
#             </tr>
#             <tr>
#                 <td class="correct">Q</td>
#                 <td class="partially_correct">U</td>
#                 <td class="incorrect">I</td>
#                 <td class="incorrect">C</td>
#                 <td class="incorrect">K</td>
#             </tr>
#             <tr>
#                 <td class="correct">Q</td>
#                 <td class="partially_correct">U</td>
#                 <td class="incorrect">I</td>
#                 <td class="incorrect">C</td>
#                 <td class="incorrect">K</td>
#             </tr>
#             <tr>
#                 <td class="correct">Q</td>
#                 <td class="partially_correct">U</td>
#                 <td class="incorrect">I</td>
#                 <td class="incorrect">C</td>
#                 <td class="incorrect">K</td>
#             </tr>
#             <tr>
#                 <td class="correct">Q</td>
#                 <td class="partially_correct">U</td>
#                 <td class="incorrect">I</td>
#                 <td class="incorrect">C</td>
#                 <td class="incorrect">K</td>
#             </tr>
#             <tr>
#                 <td></td>
#                 <td></td>
#                 <td></td>
#                 <td></td>
#                 <td></td>
#             </tr>
#         </table>
#     </div>
# <div>
# """)