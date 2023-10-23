preprocess:
	python preprocess_data.py --url_train_analysis "https://raw.githubusercontent.com/Falconwatch/Hometasks/main/diabets/data/raw/diabetes_train_analysis.csv" --url_train_info "https://raw.githubusercontent.com/Falconwatch/Hometasks/main/diabets/data/raw/diabetes_train_info.csv" --url_test_analysis "https://raw.githubusercontent.com/Falconwatch/Hometasks/main/diabets/data/raw/diabetes_test_analysis.csv" --url_test_info "https://raw.githubusercontent.com/Falconwatch/Hometasks/main/diabets/data/raw/diabetes_test_info.csv" --save_test_df_path "test_df.csv" --save_train_df_path "train_df.csv"
train:
	python train_model.py --save_test_df_path "test_df.csv" --save_train_df_path "train_df.csv"
fit:
	python fit_model.py --save_test_df_path "/content/test_df.csv" --save_train_df_path "/content/train_df.csv" --save_model_path "model_gbc_grid.pkl"
predict:
	python make_predictions.py --save_test_df_path "/content/test_df.csv" --save_train_df_path "/content/train_df.csv" --save_model_path "model_gbc_grid.pkl"
pipeline: preprocess train fit predict
