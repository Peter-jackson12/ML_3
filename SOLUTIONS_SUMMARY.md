# ML3 Solutions Summary
Completed notebooks written to `/workspace/ml3-outputs/`.
Streamlit app: `app.py` (nb_05).

## nb_01.ipynb — 1장1강 문제유형 데이터분리 평가지표 실습문제.ipynb
- cell 5: X/y, train/valid/test (~6:2:2) with random_state=42
- cell 6: Q1–Q4 Korean answers (regression roles)
- cell 8: y_train mean baseline + valid MSE/RMSE/MAE/R²
- cell 9: metric interpretation answers
- cell 11: test baseline metrics
- cell 12–13: assignment + wrap-up answers

## nb_02.ipynb — 1장2강 핵심모델 선택기준 실습문제.ipynb
- cell 5: LinearRegression fit, intercept/coef, head predictions
- cell 6: Q answers (regression vs logistic)
- cell 8: StandardScaler + KMeans(k=3) + PCA(n=2)
- cell 9–11: unsupervised Q + model-selection homework answers

## nb_03.ipynb — 2장1강 시계열 데이터 정상성 진단 실습문제.ipynb
- cell 7: daily count line plot
- cell 10: seasonal_decompose additive period=12
- cell 13: 7-day rolling mean plot
- cell 15/18: ADF on level + 1st difference
- cell 21: registered series stationarity homework
- markdown Q1–Q6 answers

## nb_04.ipynb — 2장2강 시계열 모델링과 예측 실습문제.ipynb
- cell 6: last-6-months chronological Train/Test split
- cell 10: ARIMA(2,1,1) fit on Train
- cell 12: forecast vs actual plot
- cell 16: ADF-based d selection, get_forecast 95% PI, MAE/RMSE
- Q1–Q9 interpretive answers

## nb_05.ipynb — 2장3강 Streamlit 시계열 예측 웹앱 실습문제.ipynb
- cells 4/6/9/11/14: key Streamlit/ARIMA snippets for app.py
- cell 16: points to complete app.py
- created `/workspace/ml3-outputs/app.py` full ARIMA forecasting app
- Q1–Q3 answers

## nb_06.ipynb — 3장1강 편향분산 학습곡선 검증곡선 실습문제.ipynb
- cell 5/8: learning_curve max_depth=2 vs None
- cell 11: validation_curve over max_depth → gap_df
- cell 15: diagnose depth 1/8/None
- Q1–Q6 answers

## nb_07.ipynb — 3장2강 규제 Lasso Ridge ElasticNet 실습문제.ipynb
- cell 5: Ridge alpha sweep (R² + coef L1-norm)
- cell 9/12: Lasso(alpha=1000), ElasticNet(0.1, 0.5)
- cell 15: VIF on Train + Ridge/Lasso/ElasticNet comparison tables
- Q1–Q9 answers

## nb_08.ipynb — 4장1강 데이터불균형 평가지표 왜곡 실습문제.ipynb
- cell 5: all-zero baseline Accuracy/Recall
- cell 8: LogisticRegression multi-metrics + PR-AUC + CM
- cell 11/13/15: class_weight, RandomUnderSampler, SMOTE (Train only)
- cell 18: model compare + thresholds 0.3/0.5/0.7
- Q1–Q7 answers

## nb_09.ipynb — 4장2강 교차검증 데이터 누수방지 실습문제.ipynb
- cell 5/7: KFold vs StratifiedKFold Class=1 ratios
- cell 9: F1 CV comparison
- cell 13: sklearn Pipeline(scaler+LR) Stratified CV
- cell 16: ImbPipeline(SMOTE+LR)
- cell 19: build_pipeline / evaluate_pipeline helpers
- Q1–Q8 answers

## nb_10.ipynb — 5장1강 배깅 랜덤포레스트 실습문제.ipynb
- cell 4: single DecisionTree Train/Test R²
- cell 7: BaggingRegressor n_estimators=50 max_features=sqrt
- cell 10: RF OOB score
- cell 13: feature_importances_ bar chart
- cell 16: n_estimators stability curve
- Q1–Q7 answers

## nb_11.ipynb — 5장2강 부스팅계열 모델 실습문제.ipynb
- cell 7: GradientBoosting staged_predict Test RMSE curve
- cell 10: XGB vs LGBM time/RMSE
- cell 14: learning_rate × n_estimators grid
- cell 17: XGB early stopping on internal validation
- Q1–Q7 answers

## nb_12.ipynb — 5장3강 배깅부스팅 SHAP 실습문제.ipynb
- cell 5: RF vs XGB Test RMSE/R²/time
- cell 9/12: FI + TreeSHAP global bar
- cell 15–17: Train_sub/Valid split, SHAP local top5, top-6 feature retrain comparison
- Q1–Q9 answers

## nb_13.ipynb — 6장1강 CV기반 하이퍼 파라미터튜닝 실습문제.ipynb
- cell 3: fixed Windows absolute path → Ames_Housing.csv
- cell 5/8: GridSearchCV + RandomizedSearchCV (9 trials)
- cell 11/14: Optuna TPE (9 trials) + CV std
- cell 16: search summary, baseline vs tuned same KFold, hold-out Test once, save model_artifacts
- Q1–Q7 answers

## Other deliverables
- `app.py`: complete Streamlit ARIMA monthly forecast app matching nb_05
- `requirements.txt`: package pins for running notebooks/app
- `.gitignore`: excludes data/, csv/parquet/h5/pkl, venv, checkpoints, secrets, creditcard heavy data

## Gaps / notes
- Numeric metric values are computed at runtime (not invented in markdown).
- Data files are expected beside notebooks as `Ames_Housing.csv`, `Bike_Sharing_Demand.csv`, `creditcard.csv` (same relative paths as original setup cells).
- nb_08/nb_09 use full `creditcard.csv` as in setup cells (no extra subsample added).
- Interpretive Q answers that depend on printed numbers point students to the code output.
