params = {
    'target':'interested_to_EDC_flag', 
    'target_metric': 'MCC', # 'Accuracy', 'AUC', 'Recall', 'Precision', 'F1', 'Kappa', 'MCC'
    'train_size': 0.8, 
    'numeric_features': [], 
    'categorical_features': [], 
    'ignore_features': 'phone_number_clean', 
    'imputation_type': 'simple', #‘simple’ or ‘iterative’
    'numeric_imputation': 'knn', # “drop”, “mean”, “median”, “mode”, “knn”, int or float
    'categorical_imputation': 'mode', # “drop”, “mode”, str
    'iterative_imputation_iters': 5, 
    'numeric_iterative_imputer': 'lightgbm', 
    'categorical_iterative_imputer': 'lightgbm', 
    'remove_multicollinearity': False, 
    'multicollinearity_threshold': 0.9, 
    'remove_outliers': False, 
    'fix_imbalance': True, 
    'transformation': True, 
    'normalize': True, 
    'data_split_shuffle': False, 
    'data_split_stratify': False, 
    'fold_strategy': 'stratifiedkfold', 
    'fold': 5, 
    'fold_shuffle': True, 
    'session_id': 123, 
    'require_explanation':True,
    'hyperparameter_search':False,
    'plots':['auc', 'ks', 'feature_all', 'lift'], #‘pipeline’, ‘auc’, ‘threshold’, ‘pr’, ‘confusion_matrix’, ‘error’, ‘class_report’, ‘boundary’, ‘rfe’, ‘learning’, 
    'included_models':['rf'] #['lr', 'knn', 'nb', 'dt', 'svm', 'rbfsvm', 'gpc', 'mlp', 'ridge', 'rf', 'qda', 'ada', 'gbc', 'lda', 'et', 'xgboost', 'lightgbm', 'catboost', 'dummy']
    # ‘manifold’, ‘calibration’, ‘vc’, ‘dimension’, ‘feature’, ‘feature_all’, ‘parameter’, ‘lift’, ‘gain’, ‘tree’, ‘ks’
    # 'keep_features': [], 
    # 'ordinal_features': [], 
    # 'date_features':[], 
    # 'text_features':[], 
    # 'text_features_method': 'tf-idf', # “bow” or “tf-idf”
    # 'max_encoding_ohe': 25, 
    # 'encoding_method': None, 
    # 'rare_to_value': None, 
    # 'rare_value': 'rare', 
    # 'polynomial_features': False, 
    # 'polynomial_degree': 2, 
    # 'low_variance_threshold': None, 
    # 'group_features': None, 
    # 'group_names': None, 
    # 'drop_groups': False, 
    # 'bin_numeric_features': None, 
    # 'outliers_method': 'iforest', 
    # 'outliers_threshold': 0.05, 
    # 'fix_imbalance_method': 'SMOTE', 
    # 'transformation_method': 'yeo-johnson', # ‘yeo-johnson’, ‘quantile’.
    # 'normalize_method': 'zscore', 
    # 'pca': bool = False, 
    # 'pca_method': str = 'linear', 
    # 'pca_components': None, 
    # 'feature_selection': True, 
    # 'feature_selection_method': 'classic', 
    # 'feature_selection_estimator': 'lightgbm', 
    # 'n_features_to_select': 0.2, 
}


raw_query =\
    '''
    WITH main AS (
    SELECT 
        phone_number_clean,
        '1' AS responded,
        interested_to_EDC_flag,
        ms_area,
        acquisition_channel,
        user_age,
        kyc_tier,
        loyalty_tier,
        age_on_core_days,
        age_on_ncore_days,
        age_on_accounting_days,
        referee_count,
        est_daily_customer,
        count_trf,
        edc_count,
        edc_type,
        business_age,
        core_before_shutdown_flag,
        ppob_before_shutdown_flag,
        M0_core_count,
        M0_ppob_payment_count,
        M0_QRIS_payment_count,
        LM_core_count,
        LM_ppob_payment_count,
        LM_QRIS_payment_count,
        L2M_core_count,
        L2M_ppob_payment_count,
        L2M_QRIS_payment_count,
        L3M_core_count,
        L3M_ppob_payment_count,
        L3M_QRIS_payment_count,
        M0_corepayment_TPV,
        M0_ppob_TPV,
        M0_QRIS_TPV,
        LM_corepayment_TPV,
        LM_ppob_TPV,
        LM_QRIS_TPV,
        L2M_corepayment_TPV,
        L2M_ppob_TPV,
        L2M_QRIS_TPV,
        L3M_corepayment_TPV,
        L3M_ppob_TPV,
        L3M_QRIS_TPV,
        m0_transaxi_cnt,
        m0_Utang_cnt,
        lm_transaxi_cnt,
        lm_Utang_cnt,
        m2_transaxi_cnt,
        m2_Utang_cnt,
        m3_transaxi_cnt,
        m3_Utang_cnt,
    FROM `ledger-fcc1e.dg_buku_trnsfmd.EDC_survey_userbase`

    UNION ALL

    SELECT DISTINCT
        phone_number_clean,
        responded,
        '0' AS interested_to_EDC_flag,
        ms_area,
        acquisition_channel,
        user_age,
        kyc_tier,
        loyalty_tier,
        age_on_core_days,
        age_on_ncore_days,
        age_on_accounting_days,
        referee_count,
        est_daily_customer,
        count_trf,
        edc_count,
        edc_type,
        business_age,
        core_before_shutdown_flag,
        ppob_before_shutdown_flag,
        M0_core_count,
        M0_ppob_payment_count,
        M0_QRIS_payment_count,
        LM_core_count,
        LM_ppob_payment_count,
        LM_QRIS_payment_count,
        L2M_core_count,
        L2M_ppob_payment_count,
        L2M_QRIS_payment_count,
        L3M_core_count,
        L3M_ppob_payment_count,
        L3M_QRIS_payment_count,
        M0_corepayment_TPV,
        M0_ppob_TPV,
        M0_QRIS_TPV,
        LM_corepayment_TPV,
        LM_ppob_TPV,
        LM_QRIS_TPV,
        L2M_corepayment_TPV,
        L2M_ppob_TPV,
        L2M_QRIS_TPV,
        L3M_corepayment_TPV,
        L3M_ppob_TPV,
        L3M_QRIS_TPV,
        m0_transaxi_cnt,
        m0_Utang_cnt,
        lm_transaxi_cnt,
        lm_Utang_cnt,
        m2_transaxi_cnt,
        m2_Utang_cnt,
        m3_transaxi_cnt,
        m3_Utang_cnt,
    FROM `ledger-fcc1e.dg_buku_trnsfmd.EDC_survey_userbase_all`
    WHERE phone_number_clean IS NOT NULL
    )

    SELECT * EXCEPT(responded, rn)
    FROM (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY phone_number_clean ORDER BY interested_to_edc_flag DESC) AS rn
    FROM main
    )
    WHERE rn = 1
    '''
