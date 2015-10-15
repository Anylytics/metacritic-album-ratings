% Analysis of Billboard Data

%% Step 1: Load in all the data
all_files = dir('billboard_data');

billboard_data = csvreader(fullfile('billboard_data',all_files(4).name));

albums = 