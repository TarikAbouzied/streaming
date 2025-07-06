import pandas as pd

streams_df = pd.read_csv("../data/streaming_data.csv")
survey_df = pd.read_csv("../data/survey_responses.csv")

print("streams_df columns:", streams_df.columns)
print("survey_df columns:", survey_df.columns)

artist_col = "artist"

all_artists = pd.concat([streams_df[artist_col], survey_df[artist_col]]).dropna().unique()
artist_map = {name: f"Artist_{i+1:03d}" for i, name in enumerate(all_artists)}

streams_df[artist_col] = streams_df[artist_col].map(artist_map)
survey_df[artist_col] = survey_df[artist_col].map(artist_map)

streams_df.to_csv("streaming_data_anonymized.csv", index=False)
survey_df.to_csv("survey_responses_anonymized.csv", index=False)