# Dataset research

## Candidate: UCI PhiUSIIL Phishing URL (Website)

Source: https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

The downloaded file is `PhiUSIIL_Phishing_URL_Dataset.csv`. Each row
represents a website link and its corresponding webpage. The file contains
a `URL` column, other information about the link and webpage, and a
`label` column.

## Labels I checked

I counted the labels in the downloaded file using Python:

- Phishing (`0`): 100,945
- Legitimate (`1`): 134,850
- Total: 235,795

## Initial decision

I want my program to let someone paste in a website link and get a
prediction: phishing or legitimate.

I will train it using information from the link itself. I will leave out
details that require opening the website, such as its page title and
favicon (the small icon shown in a browser tab). This lets the program
use the same kind of information when someone pastes in a new link.

This dataset is a good starting point because it includes links and their
correct labels. I still need to test how well a link-only model performs.
## Download and license

Download the dataset ZIP from the UCI source linked above. Extract
`PhiUSIIL_Phishing_URL_Dataset.csv` into this `data/` folder.

The dataset is by Arvind Prasad and Shalini Chandra and is shared under
the Creative Commons Attribution 4.0 (CC BY 4.0) license.

## Data quality check (2026-09-28)

I ran `python3 src/inspect_urls.py` from the project folder.

- Total rows: 235,795
- Blank URLs: 0
- Blank labels: 0
- URLs appearing more than once: 425
- Extra rows from repeats: 425
- URLs with conflicting labels: 0

These are exact URL repeats. Before training, I will keep one copy of
each URL and then split the data into training and test groups. This
prevents an identical link from appearing in both groups.

## Training and test split (2026-09-28)

I ran `python3 src/prepare_data.py`. The script keeps one copy of
each exact URL, shuffles the links with random seed 42, and puts 80%
in the training group and 20% in the test group.

- Unique URLs: 235,370
- Training examples: 188,296
- Test examples: 47,074
- URLs shared by both groups: 0

The test group will be held aside while training the model. This gives
me a way to check predictions on links the model has not seen during
training.