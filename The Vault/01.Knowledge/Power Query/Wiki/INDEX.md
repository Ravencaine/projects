# Power Query — Knowledge Base

## Source
- [[m-code_pdf_source]] — Microsoft Power Query M Language Reference (2025-09-16)
  - 687 M functions across 137 categories
  - All function signatures, parameters, returns, examples
  - Spec/concept chapters, gotchas, patterns, snippets

## Functions (724 total, 137 categories)

### Access (1)
[[access_database]]

### Accesscontrolentry (1)
[[accesscontrolentry_conditiontoidentities]]

### Accesscontrolkind (1)
[[accesscontrolkind_type]]

### Action (1)
[[action_witherrorcontext]]

### Activedirectory (1)
[[activedirectory_domains]]

### Adobeanalytics (1)
[[adobeanalytics_cubes]]

### Adodotnet (2)
[[adodotnet_datasource]], [[adodotnet_query]]

### Analysisservices (2)
[[analysisservices_database]], [[analysisservices_databases]]

### Azurestorage (5)
[[azurestorage_blobcontents]], [[azurestorage_blobs]], [[azurestorage_datalake]], [[azurestorage_datalakecontents]], [[azurestorage_tables]]

### Binary (16)
[[binary_approximatelength]], [[binary_buffer]], [[binary_combine]], [[binary_compress]], [[binary_decompress]], [[binary_from]], [[binary_fromlist]], [[binary_fromtext]], [[binary_infercontenttype]], [[binary_length]], [[binary_range]], [[binary_tolist]], [[binary_totext]], [[binary_view]], [[binary_viewerror]], [[binary_viewfunction]]

### Binaryencoding (1)
[[binaryencoding_type]]

### Binaryformat (20)
[[binaryformat_binary]], [[binaryformat_byte]], [[binaryformat_byteorder]], [[binaryformat_choice]], [[binaryformat_decimal]], [[binaryformat_double]], [[binaryformat_group]], [[binaryformat_length]], [[binaryformat_list]], [[binaryformat_null]], [[binaryformat_record]], [[binaryformat_signedinteger16]], [[binaryformat_signedinteger32]], [[binaryformat_signedinteger64]], [[binaryformat_single]], [[binaryformat_text]], [[binaryformat_transform]], [[binaryformat_unsignedinteger16]], [[binaryformat_unsignedinteger32]], [[binaryformat_unsignedinteger64]]

### Binaryoccurrence (1)
[[binaryoccurrence_type]]

### Buffermode (1)
[[buffermode_type]]

### Byte (1)
[[byte_from]]

### Byteorder (1)
[[byteorder_type]]

### Cdm (1)
[[cdm_contents]]

### Character (2)
[[character_fromnumber]], [[character_tonumber]]

### Combiner (5)
[[combiner_combinetextbydelimiter]], [[combiner_combinetextbyeachdelimiter]], [[combiner_combinetextbylengths]], [[combiner_combinetextbypositions]], [[combiner_combinetextbyranges]]

### Comparer (4)
[[comparer_equals]], [[comparer_fromculture]], [[comparer_ordinal]], [[comparer_ordinalignorecase]]

### Compression (3)
[[compression_deflate]], [[compression_gzip]], [[compression_type]]

### Compute (1)
[[compute_scorevector]]

### Csv (1)
[[csv_document]]

### Csvstyle (1)
[[csvstyle_type]]

### Cube (16)
[[cube_addandexpanddimensioncolumn]], [[cube_addmeasurecolumn]], [[cube_applyparameter]], [[cube_attributememberid]], [[cube_attributememberproperty]], [[cube_collapseandremovecolumns]], [[cube_dimensions]], [[cube_displayfolders]], [[cube_measureproperties]], [[cube_measureproperty]], [[cube_measures]], [[cube_parameters]], [[cube_properties]], [[cube_propertykey]], [[cube_replacedimensions]], [[cube_transform]]

### Culture (2)
[[culture_and_text_formatting]], [[culture_current]]

### Currency (1)
[[currency_from]]

### Custom (1)
[[custom_numeric_format_strings]]

### Date (57)
[[date_adddays]], [[date_addmonths]], [[date_addquarters]], [[date_addweeks]], [[date_addyears]], [[date_day]], [[date_dayofweek]], [[date_dayofweekname]], [[date_dayofyear]], [[date_daysinmonth]], [[date_endofday]], [[date_endofmonth]], [[date_endofquarter]], [[date_endofweek]], [[date_endofyear]], [[date_from]], [[date_fromtext]], [[date_isincurrentday]], [[date_isincurrentmonth]], [[date_isincurrentquarter]], [[date_isincurrentweek]], [[date_isincurrentyear]], [[date_isinnextday]], [[date_isinnextmonth]], [[date_isinnextndays]], [[date_isinnextnmonths]], [[date_isinnextnquarters]], [[date_isinnextnweeks]], [[date_isinnextnyears]], [[date_isinnextquarter]], [[date_isinnextweek]], [[date_isinnextyear]], [[date_isinpreviousday]], [[date_isinpreviousmonth]], [[date_isinpreviousndays]], [[date_isinpreviousnmonths]], [[date_isinpreviousnquarters]], [[date_isinpreviousnweeks]], [[date_isinpreviousnyears]], [[date_isinpreviousquarter]], [[date_isinpreviousweek]], [[date_isinpreviousyear]], [[date_isinyeartodate]], [[date_isleapyear]], [[date_month]], [[date_monthname]], [[date_quarterofyear]], [[date_startofday]], [[date_startofmonth]], [[date_startofquarter]], [[date_startofweek]], [[date_startofyear]], [[date_torecord]], [[date_totext]], [[date_weekofmonth]], [[date_weekofyear]], [[date_year]]

### Datetime (25)
[[datetime_addzone]], [[datetime_date]], [[datetime_fixedlocalnow]], [[datetime_from]], [[datetime_fromfiletime]], [[datetime_fromtext]], [[datetime_isincurrenthour]], [[datetime_isincurrentminute]], [[datetime_isincurrentsecond]], [[datetime_isinnexthour]], [[datetime_isinnextminute]], [[datetime_isinnextnhours]], [[datetime_isinnextnminutes]], [[datetime_isinnextnseconds]], [[datetime_isinnextsecond]], [[datetime_isinprevioushour]], [[datetime_isinpreviousminute]], [[datetime_isinpreviousnhours]], [[datetime_isinpreviousnminutes]], [[datetime_isinpreviousnseconds]], [[datetime_isinprevioussecond]], [[datetime_localnow]], [[datetime_time]], [[datetime_torecord]], [[datetime_totext]]

### Datetimezone (15)
[[datetimezone_fixedlocalnow]], [[datetimezone_fixedutcnow]], [[datetimezone_from]], [[datetimezone_fromfiletime]], [[datetimezone_fromtext]], [[datetimezone_localnow]], [[datetimezone_removezone]], [[datetimezone_switchzone]], [[datetimezone_tolocal]], [[datetimezone_torecord]], [[datetimezone_totext]], [[datetimezone_toutc]], [[datetimezone_utcnow]], [[datetimezone_zonehours]], [[datetimezone_zoneminutes]]

### Day (1)
[[day_type]]

### Db2 (1)
[[db2_database]]

### Decimal (1)
[[decimal_from]]

### Deltalake (2)
[[deltalake_metadata]], [[deltalake_table]]

### Diagnostics (3)
[[diagnostics_activityid]], [[diagnostics_correlationid]], [[diagnostics_trace]]

### Directquerycapabilities (1)
[[directquerycapabilities_from]]

### Double (1)
[[double_from]]

### Duration (13)
[[duration_days]], [[duration_from]], [[duration_fromtext]], [[duration_hours]], [[duration_minutes]], [[duration_seconds]], [[duration_support]], [[duration_torecord]], [[duration_totaldays]], [[duration_totalhours]], [[duration_totalminutes]], [[duration_totalseconds]], [[duration_totext]]

### Embedded (1)
[[embedded_value]]

### Error (1)
[[error_record]]

### Essbase (1)
[[essbase_cubes]]

### Excel (3)
[[excel_currentworkbook]], [[excel_shapetable]], [[excel_workbook]]

### Exchange (1)
[[exchange_contents]]

### Expression (3)
[[expression_constant]], [[expression_evaluate]], [[expression_identifier]]

### Expressions (1)
[[expressions_vs_values]]

### Extravalues (1)
[[extravalues_type]]

### Fabricai (1)
[[fabricai_prompt]]

### File (1)
[[file_contents]]

### Folder (2)
[[folder_contents]], [[folder_files]]

### Function (6)
[[function_from]], [[function_invoke]], [[function_invokeafter]], [[function_invokewitherrorcontext]], [[function_isdatasource]], [[function_scalarvector]]

### Geography (2)
[[geography_fromwellknowntext]], [[geography_towellknowntext]]

### Geographypoint (1)
[[geographypoint_from]]

### Geometry (2)
[[geometry_fromwellknowntext]], [[geometry_towellknowntext]]

### Geometrypoint (1)
[[geometrypoint_from]]

### Googleanalytics (1)
[[googleanalytics_accounts]]

### Graph (1)
[[graph_nodes]]

### Groupkind (1)
[[groupkind_type]]

### Guid (1)
[[guid_from]]

### Hdfs (2)
[[hdfs_contents]], [[hdfs_files]]

### Hdinsight (3)
[[hdinsight_containers]], [[hdinsight_contents]], [[hdinsight_files]]

### Html (1)
[[html_table]]

### Identity (2)
[[identity_from]], [[identity_ismemberof]]

### Identityprovider (1)
[[identityprovider_default]]

### Informix (1)
[[informix_database]]

### Int16 (1)
[[int16_from]]

### Int32 (1)
[[int32_from]]

### Int64 (1)
[[int64_from]]

### Int8 (1)
[[int8_from]]

### Itemexpression (2)
[[itemexpression_from]], [[itemexpression_item]]

### Joinalgorithm (1)
[[joinalgorithm_type]]

### Joinkind (9)
[[joinkind_fullouter]], [[joinkind_inner]], [[joinkind_leftanti]], [[joinkind_leftouter]], [[joinkind_leftsemi]], [[joinkind_rightanti]], [[joinkind_rightouter]], [[joinkind_rightsemi]], [[joinkind_type]]

### Joinside (1)
[[joinside_type]]

### Json (2)
[[json_document]], [[json_fromvalue]]

### Lazy (2)
[[lazy_list_record_evaluation_gotcha]], [[lazy_vs_eager_evaluation]]

### Limitclausekind (1)
[[limitclausekind_type]]

### Lines (4)
[[lines_frombinary]], [[lines_fromtext]], [[lines_tobinary]], [[lines_totext]]

### List (71)
[[list_accumulate]], [[list_alltrue]], [[list_alternate]], [[list_anytrue]], [[list_average]], [[list_buffer]], [[list_combine]], [[list_conformtopagereader]], [[list_contains]], [[list_containsall]], [[list_containsany]], [[list_count]], [[list_covariance]], [[list_dates]], [[list_datetimes]], [[list_datetimezones]], [[list_difference]], [[list_distinct]], [[list_durations]], [[list_findtext]], [[list_first]], [[list_firstn]], [[list_generate]], [[list_insertrange]], [[list_intersect]], [[list_isdistinct]], [[list_isempty]], [[list_last]], [[list_lastn]], [[list_matchesall]], [[list_matchesany]], [[list_max]], [[list_maxn]], [[list_median]], [[list_min]], [[list_minn]], [[list_mode]], [[list_modes]], [[list_nonnullcount]], [[list_numbers]], [[list_percentile]], [[list_positionof]], [[list_positionofany]], [[list_positions]], [[list_product]], [[list_random]], [[list_range]], [[list_removefirstn]], [[list_removeitems]], [[list_removelastn]], [[list_removematchingitems]], [[list_removenulls]], [[list_removerange]], [[list_repeat]], [[list_replacematchingitems]], [[list_replacerange]], [[list_replacevalue]], [[list_reverse]], [[list_select]], [[list_single]], [[list_singleordefault]], [[list_skip]], [[list_sort]], [[list_split]], [[list_standarddeviation]], [[list_sum]], [[list_times]], [[list_transform]], [[list_transformmany]], [[list_union]], [[list_zip]]

### Logical (3)
[[logical_from]], [[logical_fromtext]], [[logical_totext]]

### M-Code (1)
[[m-code_pdf_source]]

### Missingfield (3)
[[missingfield_ignore]], [[missingfield_type]], [[missingfield_usenull]]

### Module (1)
[[module_versions]]

### Mysql (1)
[[mysql_database]]

### Number (47)
[[number_abs]], [[number_acos]], [[number_asin]], [[number_atan]], [[number_atan2]], [[number_bitwiseand]], [[number_bitwisenot]], [[number_bitwiseor]], [[number_bitwiseshiftleft]], [[number_bitwiseshiftright]], [[number_bitwisexor]], [[number_combinations]], [[number_cos]], [[number_cosh]], [[number_epsilon]], [[number_exp]], [[number_factorial]], [[number_from]], [[number_fromtext]], [[number_integerdivide]], [[number_iseven]], [[number_isnan]], [[number_isodd]], [[number_ln]], [[number_log]], [[number_log10]], [[number_mod]], [[number_nan]], [[number_negativeinfinity]], [[number_permutations]], [[number_pi]], [[number_positiveinfinity]], [[number_power]], [[number_random]], [[number_randombetween]], [[number_round]], [[number_roundawayfromzero]], [[number_rounddown]], [[number_roundtowardzero]], [[number_roundup]], [[number_sign]], [[number_sin]], [[number_sinh]], [[number_sqrt]], [[number_tan]], [[number_tanh]], [[number_totext]]

### Occurrence (2)
[[occurrence_all]], [[occurrence_type]]

### Odata (1)
[[odata_feed]]

### Odataomitvalues (1)
[[odataomitvalues_type]]

### Odbc (3)
[[odbc_datasource]], [[odbc_inferoptions]], [[odbc_query]]

### Oledb (2)
[[oledb_datasource]], [[oledb_query]]

### Oracle (1)
[[oracle_database]]

### Order (1)
[[order_type]]

### Pdf (1)
[[pdf_tables]]

### Percentage (1)
[[percentage_from]]

### Percentilemode (1)
[[percentilemode_type]]

### Postgresql (1)
[[postgresql_database]]

### Pq (1)
[[pq_text_case_sensitive_vs_power_bi_normalization]]

### Precision (1)
[[precision_type]]

### Progress (1)
[[progress_datasourceprogress]]

### Quoted (1)
[[quoted_identifier_syntax]]

### Quotestyle (1)
[[quotestyle_type]]

### Rankkind (1)
[[rankkind_type]]

### Rdata (1)
[[rdata_frombinary]]

### Record (18)
[[record_addfield]], [[record_and_list_lookup]], [[record_combine]], [[record_field]], [[record_fieldcount]], [[record_fieldnames]], [[record_fieldordefault]], [[record_fieldvalues]], [[record_fromlist]], [[record_fromtable]], [[record_hasfields]], [[record_removefields]], [[record_renamefields]], [[record_reorderfields]], [[record_selectfields]], [[record_tolist]], [[record_totable]], [[record_transformfields]]

### Relativeposition (1)
[[relativeposition_type]]

### Replacer (2)
[[replacer_replacetext]], [[replacer_replacevalue]]

### Roundingmode (1)
[[roundingmode_type]]

### Rowexpression (3)
[[rowexpression_column]], [[rowexpression_from]], [[rowexpression_row]]

### Salesforce (2)
[[salesforce_data]], [[salesforce_reports]]

### Sapbusinesswarehouse (1)
[[sapbusinesswarehouse_cubes]]

### Sapbusinesswarehouseexecutionmode (1)
[[sapbusinesswarehouseexecutionmode_typ]]

### Saphana (1)
[[saphana_database]]

### Saphanadistribution (1)
[[saphanadistribution_type]]

### Saphanarangeoperator (1)
[[saphanarangeoperator_type]]

### Sharepoint (3)
[[sharepoint_contents]], [[sharepoint_files]], [[sharepoint_tables]]

### Single (1)
[[single_from]]

### Soda (1)
[[soda_feed]]

### Splitter (10)
[[splitter_splitbynothing]], [[splitter_splittextbyanydelimiter]], [[splitter_splittextbycharactertransition]], [[splitter_splittextbydelimiter]], [[splitter_splittextbyeachdelimiter]], [[splitter_splittextbylengths]], [[splitter_splittextbypositions]], [[splitter_splittextbyranges]], [[splitter_splittextbyrepeatedlengths]], [[splitter_splittextbywhitespace]]

### Sql (2)
[[sql_database]], [[sql_databases]]

### Sqlexpression (2)
[[sqlexpression_schemafrom]], [[sqlexpression_toexpression]]

### Standard (2)
[[standard_date_and_time_format_strings]], [[standard_numeric_format_strings]]

### Sybase (1)
[[sybase_database]]

### Table (114)
[[table_addcolumn]], [[table_addfuzzyclustercolumn]], [[table_addindexcolumn]], [[table_addjoincolumn]], [[table_addkey]], [[table_addrankcolumn]], [[table_aggregatetablecolumn]], [[table_alternaterows]], [[table_approximaterowcount]], [[table_buffer]], [[table_column]], [[table_columncount]], [[table_columnnames]], [[table_columnsoftype]], [[table_combine]], [[table_combinecolumns]], [[table_combinecolumnstorecord]], [[table_conformtopagereader]], [[table_contains]], [[table_containsall]], [[table_containsany]], [[table_demoteheaders]], [[table_distinct]], [[table_duplicatecolumn]], [[table_expandlistcolumn]], [[table_expandrecordcolumn]], [[table_expandtablecolumn]], [[table_filldown]], [[table_fillup]], [[table_filterwithdatatable]], [[table_findtext]], [[table_first]], [[table_firstn]], [[table_firstvalue]], [[table_fromcolumns]], [[table_fromlist]], [[table_frompartitions]], [[table_fromrecords]], [[table_fromrows]], [[table_fromvalue]], [[table_fuzzygroup]], [[table_fuzzyjoin]], [[table_fuzzynestedjoin]], [[table_group]], [[table_hascolumns]], [[table_insertrows]], [[table_isdistinct]], [[table_isempty]], [[table_join]], [[table_keys]], [[table_last]], [[table_lastn]], [[table_literal_syntax]], [[table_matchesallrows]], [[table_matchesanyrows]], [[table_max]], [[table_maxn]], [[table_min]], [[table_minn]], [[table_nestedjoin]], [[table_partition]], [[table_partitionkey]], [[table_partitionvalues]], [[table_pivot]], [[table_positionof]], [[table_positionofany]], [[table_prefixcolumns]], [[table_profile]], [[table_promoteheaders]], [[table_range]], [[table_removecolumns]], [[table_removefirstn]], [[table_removelastn]], [[table_removematchingrows]], [[table_removerows]], [[table_removerowswitherrors]], [[table_renamecolumns]], [[table_reordercolumns]], [[table_repeat]], [[table_replaceerrorvalues]], [[table_replacekeys]], [[table_replacematchingrows]], [[table_replacepartitionkey]], [[table_replacerelationshipidentity]], [[table_replacerows]], [[table_replacevalue]], [[table_reverserows]], [[table_rowcount]], [[table_schema]], [[table_selectcolumns]], [[table_selectrows]], [[table_selectrowswitherrors]], [[table_singlerow]], [[table_skip]], [[table_sort]], [[table_split]], [[table_splitat]], [[table_splitcolumn]], [[table_stopfolding]], [[table_tocolumns]], [[table_tolist]], [[table_torecords]], [[table_torows]], [[table_transformcolumnnames]], [[table_transformcolumns]], [[table_transformcolumntypes]], [[table_transformrows]], [[table_transpose]], [[table_unpivot]], [[table_unpivotothercolumns]], [[table_view]], [[table_viewerror]], [[table_viewfunction]], [[table_witherrorcontext]]

### Tables (1)
[[tables_getrelationships]]

### Teradata (1)
[[teradata_database]]

### Text (41)
[[text_afterdelimiter]], [[text_at]], [[text_beforedelimiter]], [[text_betweendelimiters]], [[text_clean]], [[text_combine]], [[text_contains]], [[text_end]], [[text_endswith]], [[text_format]], [[text_from]], [[text_frombinary]], [[text_infernumbertype]], [[text_insert]], [[text_length]], [[text_lower]], [[text_middle]], [[text_newguid]], [[text_padend]], [[text_padstart]], [[text_positionof]], [[text_positionofany]], [[text_proper]], [[text_range]], [[text_remove]], [[text_removerange]], [[text_repeat]], [[text_replace]], [[text_replacerange]], [[text_reverse]], [[text_select]], [[text_split]], [[text_splitany]], [[text_start]], [[text_startswith]], [[text_tobinary]], [[text_tolist]], [[text_trim]], [[text_trimend]], [[text_trimstart]], [[text_upper]]

### Textencoding (2)
[[textencoding_ascii]], [[textencoding_type]]

### Time (9)
[[time_endofhour]], [[time_from]], [[time_fromtext]], [[time_hour]], [[time_minute]], [[time_second]], [[time_startofhour]], [[time_torecord]], [[time_totext]]

### Timezone (1)
[[timezone_current]]

### Tracelevel (6)
[[tracelevel_critical]], [[tracelevel_error]], [[tracelevel_information]], [[tracelevel_type]], [[tracelevel_verbose]], [[tracelevel_warning]]

### Type (24)
[[type_addtablekey]], [[type_closedrecord]], [[type_facets]], [[type_forfunction]], [[type_forrecord]], [[type_functionparameters]], [[type_functionrequiredparameters]], [[type_functionreturn]], [[type_is]], [[type_isnullable]], [[type_isopenrecord]], [[type_listitem]], [[type_nonnullable]], [[type_openrecord]], [[type_recordfields]], [[type_replacefacets]], [[type_replacetablekeys]], [[type_replacetablepartitionkey]], [[type_tablecolumn]], [[type_tablekeys]], [[type_tablepartitionkey]], [[type_tablerow]], [[type_tableschema]], [[type_union]]

### Uri (4)
[[uri_buildquerystring]], [[uri_combine]], [[uri_escapedatastring]], [[uri_parts]]

### Value (26)
[[value_add]], [[value_alternates]], [[value_as]], [[value_compare]], [[value_divide]], [[value_equals]], [[value_expression]], [[value_firewall]], [[value_fromtext]], [[value_is]], [[value_lineage]], [[value_metadata]], [[value_multiply]], [[value_nativequery]], [[value_nullableequals]], [[value_optimize]], [[value_removemetadata]], [[value_replacemetadata]], [[value_replacetype]], [[value_subtract]], [[value_traits]], [[value_type]], [[value_versionidentity]], [[value_versions]], [[value_viewerror]], [[value_viewfunction]]

### Variable (2)
[[variable_value]], [[variable_valueordefault]]

### Web (4)
[[web_browsercontents]], [[web_contents]], [[web_headers]], [[web_page]]

### Webaction (1)
[[webaction_request]]

### Webmethod (1)
[[webmethod_type]]

### Xml (2)
[[xml_document]], [[xml_tables]]

## M Consolidated References (18)
- [[m_consolidated_grammar]]
- [[m_error_handling_with_try]]
- [[m_evaluation_model]]
- [[m_function_reference_index]]
- [[m_functions_as_values]]
- [[m_if_expressions]]
- [[m_language_is_functional_and_case_sensitive]]
- [[m_let_expressions]]
- [[m_lexical_structure]]
- [[m_metadata]]
- [[m_operator_behaviour]]
- [[m_operators]]
- [[m_operators_operand_dependent_meaning]]
- [[m_primitive_types]]
- [[m_query_structure_let_in]]
- [[m_sections]]
- [[m_standard_library]]
- [[m_type_system]]

## System
- [[INDEX]]
- [[QUESTIONS]]
