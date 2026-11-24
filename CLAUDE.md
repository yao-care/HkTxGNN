# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）；
UsTxGNN 是第一個試做站（做法見 UsTxGNN/CLAUDE.md 同名一節）。本站的規則與程式都在本 repo，頁面文字用繁體中文（香港用語），依據是衞生署藥物辦公室的藥劑製品註冊資料（DrugList.xml，只收現行在列）。
本站的在地字樣、頁首規則細節、歷史刪改的提交清單集中在 `src/hktxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁在免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/hktxgnn/regulatory/page_format.py` | 頁首＝快速總覽「證據等級」格的**第一個**等級（主預測）。2026-11-12 實測 876 頁有總覽等級，頁首全部符合（0 頁例外），所以照實寫成程式、不改現有等級；Tw 是整格取最高，本站不同。頁首已是 N/A 的頁不依總覽格重算 |
| 撤回預測 | `src/hktxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/hk_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/hktxgnn/regulatory/licenses.py` | 快照存本藥許可證號與事實層；gate 依快照驗市場段落表格的許可證號屬於本藥、狀態列與張數列＝事實層寫法、表格列狀態不跟事實相反（本站沒有程式產生的許可證表，不驗表格列內容） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證與待重審項目；證據包沒有許可證適應症文字時照實回報可比對 0 頁 |
| gate | `scripts/check_seo_docs.py` 最後 4 項 | 紀錄都已套用、許可證＝快照、頁首＝快速總覽等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依新事實直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 1 筆紀錄（1 頁）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁後會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。


## 新資料查不到的註冊號（2026-11-17）

11-16 每週排程列出 146 張「新資料查不到」的註冊號（涵蓋 98.2%，沒開 issue）。2026-11-17 用戶要求確認實際狀態：
藥物辦公室只公開一份註冊名單 DrugList.xml（data.gov.hk「List of Registered Pharmaceutical Products」；DrugList-v1.1.xml 內容相同），只列現行註冊、沒有狀態欄，
也沒有另一份現行或已取消註冊的清單；146 張都是 HK-xxxxx 標準寫法，不是號碼寫法差異。
- 146 張全部在 data.gov.hk 歷史存檔的每週 DrugList.xml（2025-08-04 起）裡出現過，最後一次分別在 2026-03-02～11-02 的版本，2026-11-13 版（現行）沒有；
  藥物辦公室網上「搜尋藥物資料庫」依註冊號查也是 0 筆。沒有找到「在別份現行清單上」的號。名單不分取消註冊或沒有續期，頁面一律寫「已註銷」。
  其中 10 張有同品名、另一個註冊號的現行註冊（例 JADENU HK-64787→HK-68030、ATECTURA 3 張→HK-68048～68050、ZEJULA HK-65945→HK-67238），是另一張註冊，舊號仍算註銷；
  新號多半已在證據包，ezetimibe（HK-69166）、metformin（HK-56689）兩張現行註冊不在證據包（同日以 scripts/add_current_registrations.py 補收，見下）。
- `scripts/license_adapter.py`：fetch() 把名單的註冊號記成 CURRENT（少於 10,000 不判定）；preprocess 對名單沒有的 HK-xxxxx 標
  `license_status: cancelled`＋`drugoffice_not_listed`（第一次發現日），又出現就取消；`confirmed_absent()` 讓排程把這些列成「主管機關現行清單確認已不列」，不算「查不到」、不開 issue。
- 86 頁狀態列／張數列照事實層同步；正文寫「全部有效／無已註銷」或有效張數跟事實相反的 56 頁以 57 筆 `hk-lic-20261117-*`、表格狀態欄寫「有效」的 5 頁 6 列以 `hk-row-20261117-*` 更正
  （部分紀錄的頁改成「至少 N 張有效（本次收錄 20 張，其中 …已註銷）」）。全部註銷的 8 個藥依成分對名單確認現行 0 個產品：andexanet alfa、caspofungin、exenatide、
  interferon beta-1b（現行只有 1a）、naftidrofuryl、narasin、reserpine、tazemetostat（exenatide、narasin 沒有藥物頁）。
- 補收現行名單上、證據包收不到的本藥註冊號（同日）：證據包是 2026-03 版 DrugList.xml＋drug_mapping.csv 收的（藥名→DrugBank ID→同 ID 的註冊號，單方複方都收，最多 20 筆），
  之後新註冊的 302 個號不在 drug_mapping、永遠收不進來。`scripts/add_current_registrations.py --xml <現行 DrugList.xml>` 照同一套規則補收（同一支 map_fda_drugs_to_drugbank 對 DrugBank ID，不放寬）：
  A. 2026-03 版之後新增、DrugBank ID 跟證據包相交的號（313 筆，total_matches 同步加）；B. 證據包裡已註銷的號、現行名單有同產品名同成分的另一個號而證據包因 20 筆上限沒收到（metformin HK-54377→HK-56689，2 個證據包）。
  151 個證據包補 315 筆（ezetimibe HK-69166 屬 A）；102 頁狀態列／張數列由程式同步；正文張數跟新事實矛盾的 33 頁以 `hk-lic-20261117-*`（新 25 筆、同 id 重發 10 筆，前版存 history）更正。
  其他因 20 筆上限沒收的舊號不補（證據包照舊算部分收錄，頁面寫「至少 N 張」）。這支沒有接進每週排程，之後新註冊的號要再跑一次。
- 拿掉證據包 20 筆上限（同日，用戶決定）：`add_current_registrations.py` 預設改做 C——照原收錄規則補齊本藥全部註冊號（2026-03 版名單上的號照 drug_mapping.csv 的 DrugBank ID，
  之後新增的號照 A 的 map_fda_drugs_to_drugbank；不放寬），現行名單有的補成現行紀錄，2026-03 版有、現行名單已不列的補成已註銷（drugoffice_not_listed，同 license_adapter）；
  補完 total_matches＝紀錄數、`tfda.complete`＝名單 lastUpdate，證據包不再是 partial（drug_evidence_pack 的 partial＝total_matches 大於紀錄數）。可重複執行、只加不刪，每筆記 source／added；`--no-complete` 是舊行為。
  2026-11-17 跑 2026-11-13 版名單：300 個證據包補 18,171 筆（現行 17,803、已不列 368；含 17 個原本就算完整、但 drug_mapping 對到的號比證據包多的證據包，例 testosterone 2→5 張），
  部分收錄的證據包 283→0；171 頁狀態列／張數列由程式同步（165 頁從「至少 N 張」變完整張數，例 acetaminophen 至少 22→709 張中 693 張有效、amoxicillin→156 張中 153 張有效）。
  正文依舊證據包寫的張數、「至少 N 張」「清單可能不完整」、「皆為有效／皆為單一成分／無已註銷」以 154 筆新 `hk-lic-20261117-*`（142 頁，含 6 格快速總覽「核准數」列）、26 筆同 id 重發（前版存 history）更正，
  統一寫成「香港共有 N 張含本藥成分的許可證（有效 V 張、已註銷 C 張；單一成分 S 張、複方 M 張）」；單一成分／複方照註冊名單 activeIng 個數（事實層的 valid_single 用「;;」切，HK 每張都算單方，不能用）。
  原文的單方說法有不少跟事實相反（例 alanine、isoleucine 等胺基酸、amylmetacresol 實為全部複方）。更正後保留了原文劑型全稱說法（「皆為眼藥水」「皆為錠劑」等，依舊證據包前 20 張寫的）的 10 句、
  sulfadiazine 的「其餘 15 張…」子集說法 1 句，劑型沒有逐張確認，列進 drug_reviews_uncertain.json（open）。每週排程跑的是同一支（預設 C），之後新註冊或新對到的號會自動補齊、證據包維持完整；正文要另寫紀錄。
  母目錄 check_drug_page.py 對 clopidogrel（「並不代表對所有偏頭痛患者有效」，臨床句）、piroxicam（「所有已列許可證皆為單一成分製劑、狀態有效」，上表 5 張確實有效）報 M3c，是頁面變完整後才會判的誤報，沒改。
- 原本就有、跟這次無關：nitroprusside 公開頁沒有 MedicationKnowledge（front matter 沒有 drugbank_id）——同日 080468cc9 已補（drugbank_id DB00325 取自證據包，MK 與 9 筆 CUD 從 git 歷史找回、跟 predicted_indications 相同），2026-11-19 sync_fhir_levels 確認一致。
- 2026-11-19 待查清單的 11 筆劑型說法逐張對照已補齊的證據包（2026-11-13 版名單，劑型依產品名）：amylmetacresol（皆為含片）、ephedrine、formoterol（皆為吸入劑）、ketoconazole（乳膏與洗髮水為主）、mepyramine（皆為乳膏）、potassium_chloride 6 句成立，標 resolved；fexofenadine（另有 1 張口服混懸液 HK-60536）、hypromellose（另有 1 張眼用凝膠 HK-51887）、tacrolimus（另有 1 張輸注用濃縮液 HK-41917）、triamcinolone（另有 2 張注射劑 HK-16824、HK-23798）4 句不成立，以 hk-lic-20261117-*-1 同 id 重發改寫（前版存 history；新紀錄錨在舊紀錄的更正文字上會讓舊紀錄找不到錨點，所以不另開新 id）；sulfadiazine「其餘 15 張」→「其餘 18 張皆為乳膏」以 `hk-lic-20261119-sulfadiazine-1` 更正。
- 2026-11-17 起每週排程（license-refresh.yml）在 license_refresh 前先下載現行 DrugList.xml 跑 `scripts/add_current_registrations.py`，新註冊的本藥號碼會自動補進證據包；有補收就照常發新 Release。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 871 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「目前缺乏詳細的作用機轉資料。」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `hk-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（繁體中文）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：708 頁寫入紀錄（美國仿單 634、ChEMBL 74），163 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；同頁第二句起補 3 筆紀錄（id 結尾 -2）；ChEMBL 譯文（詞組清單）後補句號 74 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 2 筆紀錄；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）2 筆改成那句在節錄前（原文不改，只換順序）；同頁重複引用同一段節錄的 5 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「原適應症：本地許可證資料未記載適應症」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：衞生署藥劑製品註冊。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abacavir「原適應症：本地許可證資料未記載適應症」→「香港藥劑製品註冊：10 張（有效 10 張）」；2026-11-19 改了 459 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site HkTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 許可證表與正文張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（跨站「許可證張數與狀態不再每週過期」）：每週許可證排程只改得到概覽表的狀態列／張數列，市場段落 AI 寫的自由格式許可證表與正文寫死的張數會跟著主管機關資料過期、被 checker 擋下。本站兩件都做：
- A. 程式許可證表：`scripts/sync_license_tables.py` 把「## 香港上市資訊」的第一張表（2026-11-24 前 944 頁有 AI 表，813 頁是「| 許可證號 | 品名 | 劑型 | 核准適應症 |」、劑型與適應症欄全是「未記錄」）換成
  「| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |」，資料是證據包 tfda.records（DrugList.xml；add_current_registrations.py 已補齊全部註冊），前後 `<!-- licenses:begin/end -->`。
  選列：換表當時 AI 原表依序列的號存在 `config/license_table_pins.json`（944 頁），程式表照這個順序列（正文常寫「以上 5 張…」「另有 HK-xxxxx…」「其餘包括 …」，換成別的列會對不上）；
  原本沒有表的 6 頁與補位照程式排序（單一成分在前、同類中有效在前、再依許可證號）。列數＝原表列數（最多 20），總數較多時表下加「上表列出其中 N 張（共 M 張）。」。
  類別照註冊名單 activeIng 個數（「;」分隔，跟 2026-11-17 紀錄同一算法；成分欄的「-」2026-11-24 第三輪起不算成分，見下文）；狀態：有效／已註銷（license_status＝cancelled）；品名照原文，只把重量單位 KG 寫成小寫 kg（checker P5 會把大寫 KG 當知識圖譜字樣，monensin、moxidectin 2 頁）。
  套用 950 頁（含 noindex；轉址頁不動）；表上原本錨著的 6 筆 `hk-row-20261117-*` 標 `status: superseded`＋`superseded_by`（紀錄保留、頁面不顯示框）。
  接進：每週排程 `scripts/license_adapter.py` 的 sync_tables（全站重排；PAGE_NOTE 認程式說明句與標記）、`scripts/sync_notes_to_docs.py`（carry_block 移植舊頁程式區塊，寫完再跑 sync_license_tables）、
  `scripts/build_license_snapshot.py`（快照另存 rows、nrows、mix），gate 第 18 項（`src/hktxgnn/regulatory/licenses.py`：程式區塊＝快照重算、市場段落沒有程式區塊以外的表）。
- B. 正文張數程式改寫：`scripts/rewrite_license_counts.py`、`src/hktxgnn/regulatory/count_prose.py`（移植 Kr／My；中文句型）。只改阿拉伯數字＋「張」、角色明確的總數／有效／註銷數；
  有保留、相對數（另有、其餘）、講資料或查詢、劑型或廠商子集（只看數字所在子句）、顯示筆數、partial 頁、查核紀錄 replacement／anchor 所在句不動；
  單一成分／複方數字只驗不改（2026-11-17 前的報告依舊證據包「;;」切法把全部張數寫成「N 張有效單方」，只換數字會留下錯的「單方」字樣）；改成 0 張、原數字 0、中文數字（跟事實與程式表列數都不符時）不改、列出。
  `apply_drug_reviews.py`（非 --check）結尾與 `build_license_snapshot.py` 寫完快照後自動跑；gate 第 22 項擋「再跑一次會變」。
  2026-11-24 全站跑：現行正文的總數／有效／註銷數都已跟事實層一致（11-17 已更正），改寫 0 句；判斷不了的 31 句（30 頁，全是 single-combo）以 `--uncertain` 列進待查清單。
  模擬事實變動（每頁有效 −1、註銷 +1）時改寫 41 句、39 頁，其餘句型照規則不動。
- 驗證：checker 全量改前 0／改後 0；`--row-status` 0 列；gate exit 0；另寫的寬偵測（正文寫死張數或「全部有效」且跟事實層不符）剩 3 句，都是「其餘 N 張／另有 N 張」相對數（N＝總數減表列數，跟事實一致）。
- 還沒解決：每週排程的 checker（3c）在 4b 重套紀錄（含正文張數改寫）之前跑，正文張數因新事實矛盾的頁仍會先被擋下；要由母目錄 license_refresh 把改寫提前或 checker 之後重跑才會真的不擋。
  2026-11-17 的「香港共有 N 張含本藥成分的許可證（…）」全在查核紀錄 replacement 裡（135 句），照規則不改，事實變了要重發紀錄。

## 單一成分／複方舊錯句與查核紀錄更正文字的張數（2026-11-24 第二輪）

用戶 2026-11-24 第二輪決定：第一輪列進待查的舊錯句逐句寫查核紀錄更正；查核紀錄更正文字裡寫死的張數／舊表筆數同 id 重發成不寫數字。單一成分／複方一律照註冊名單成分欄（證據包 tfda.records 的 ingredients＝activeIng，「;」分隔、個數 >1 為複方，跟 11-17 紀錄與程式表「類別」欄同一算法；事實層 single_total 用「;;」切、每張都算單方，不能用）。
- 更正文字的張數（第 6 條）：11-17 的「香港共有 N 張含本藥成分的許可證（有效 V 張、已註銷 C 張；單一成分 S 張、複方 M 張）」135 筆，改成「香港含本藥成分的許可證{皆為單一成分／皆為複方／包括單一成分與複方製劑}，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表」；
  其他寫法 88 筆（「共 N 張…（V 張有效；HK-… 已註銷）」、快速總覽「核准數」格「N 張（…）」→「見上列「許可證數」（…）」、「共 N 張含本藥成分的許可證，…」、11-19 sulfadiazine「其餘 18 張」、11-24 piroxicam「上表所列 5 張」等）同樣改寫；
  說明（note）裡的張數 13 筆一併改。哪張註銷、單一成分／複方、劑型等更正的事實內容保留（點名的許可證號照列）；舊表筆數「以下列出 5 張」改「部分」。都同 id 重發，前版存 history（reason：程式許可證表／正文張數改由程式維護）。
  重發時順帶更正了更正文字本身的單方說法錯誤：carbinoxamine（全部複方）、lincomycin（MICOSPECTONE 獸用為複方）、medroxyprogesterone_acetate、polyvinyl_alcohol、fluorouracil（VERRUMAL 為複方）、aminocaproic_acid（兩張皆為複方）。
- 舊錯句（第 1 條）：待查清單 31 句 single-combo（例 cinchocaine「19 張有效單方製劑許可證」，19 張全是複方）、第一輪偵測的 6 句「以上…皆為單方」（esculin、potassium_acetate、resorcinol、sulfamethoxazole；efmoroctocog_alfa、eftrenonacog_alfa 見下）、
  另寫的寬偵測（正文講單一成分／複方的全稱或張數跟 mix 不符）另找到的同類句 40 句（另 aminocaproic_acid 1 句在 11-17 紀錄的更正文字裡，同 id 重發），共 77 筆 `hk-lic-20261124b-<藥>-N`（74 頁）更正；更正文字不寫死張數。待查清單 31 項標 resolved（附 record_ids）。
- 判定成立、沒改：efmoroctocog_alfa、eftrenonacog_alfa、albutrepenonacog_alfa、lonoctocog_alfa、moroctocog_alfa、cetrorelix、sotatercept、terlipressin 的「均為單一成分」——
  註冊名單成分欄是「-; <本藥>」（粉末＋溶劑包裝），只有一個有效成分；程式表「類別」照 activeIng 個數把這些列成「複方」，跟正文看起來矛盾，2026-11-24 第三輪用戶決定「-」不算成分，見下一節。
- 張數樣板（第 5 條）：`src/hktxgnn/regulatory/site.py` 的 FIGURES（reviews_from_edits.py 寫紀錄說明用）改成不寫數字。
- 驗證：checker 全量改前 0／改後 0（中途一版寫「含有效、已註銷張數」被 M3b 當成註銷說法擋 28 頁，改成「張數與有效張數」）；gate exit 0；寬偵測改前 95 句、改後 9 句（8 句是上面的「-」、1 句 trazodone「另有 6 張…（共 11 張）」相對數成立）。

## 成分欄的「-」不算成分、缺市場段落補程式表（2026-11-24 第三輪）

用戶 2026-11-24 第三輪決定：
- 註冊名單成分欄寫「-; <本藥>」（粉末＋溶劑包裝，溶劑那格寫「-」）時，「-」不算一個成分。`scripts/sync_license_tables.py` 的 is_combo 改用 ingredients_of（只算有字母或數字的項），
  mix（快照、正文張數改寫）與程式表「類別」欄跟著改；本站其他判單方／複方的程式沒有用 activeIng 個數（add_current_registrations.py 的成分比對是判斷同一產品，不受影響）。
  有「-」的證據包 32 個：23 個變成全部單一成分（albutrepenonacog_alfa、cetrorelix、docetaxel、efmoroctocog_alfa、eftrenonacog_alfa、lonoctocog_alfa、moroctocog_alfa、risperidone、sotatercept、terlipressin 等），
  ceftriaxone、spectinomycin、trastuzumab 仍有真正的複方；glucosamine、lignocaine、levonorgestrel、protein_c、sodium_chloride 的「-」項另有兩個以上成分，仍是複方。程式表類別改 13 頁。
  「均為單一成分」等正文（efmoroctocog_alfa、eftrenonacog_alfa、albutrepenonacog_alfa、lonoctocog_alfa、moroctocog_alfa、cetrorelix、sotatercept、perflubutane）現在跟表一致。
  依「-」算成複方而寫「包括單一成分與複方製劑」的查核紀錄更正文字 2 筆同 id 重發（`hk-lic-20261117-docetaxel-1`、`hk-lic-20261117-risperidone-1` 改「皆為單一成分」，前版存 history）；ceftriaxone 那筆仍有複方、不改；11-24、11-24b 其他紀錄沒有因「-」而錯的。
  同類複查（寬偵測：正文「皆為單一成分／單方」「皆為複方」「包括單一成分與複方」對 mix 與緊接程式表的類別欄）另找到 2 句第二輪漏掉的「皆為單方」（abiraterone 的 AKEEGA、crotamiton 的 HK-01168／HK-47770 是複方），以 `hk-lic-20261124c-<藥>-1` 更正；複查後 0 句。
  另修：第二輪重發的紀錄 summary（查核紀錄表「項目」欄）停在中途版本的「張數（含有效、」，100 筆照現行 replacement 重算（只改顯示摘要）。
- B：公開頁沒有「## 香港上市資訊」段落、但證據包有紀錄的（carvedilol 1 頁），`sync_license_tables.py` 的 add_section 在「## 安全性考量」之前（沒有就「結論與下一步」「免責聲明」之前）補段落與程式表（比照 JpTxGNN 第二輪）；noindex 頁不補。
  gate（`src/hktxgnn/regulatory/licenses.py` page_problems）擋「公開頁有證據包紀錄卻沒有市場段落」；license_adapter 的 PAGE_NOTE 放行「## 香港上市資訊」標題行。
- 驗證：checker 全量改前 0／改後 0、--row-status 0；gate exit 0；正文張數改寫 0 句、判斷不了 0 句。證據包沒有改，不用 data-overlay。

## 事實層單一成分／複方依本站成分欄切分（2026-11-24）

用戶 2026-11-24 決定：事實層依各站成分欄正確切分。reviewer/drug_evidence_pack.py 原本用「;;」切成分，本站成分欄（activeIng）以「; 」分隔，每張都算單一成分（事實層 single_total＝total）；改用 `src/hktxgnn/regulatory/ingredients.py`（同 scripts/sync_license_tables.py 程式表的類別欄，「-」不算成分）。
事實層 1550 藥中 609 藥 single_total 改變，跟快照 mix 951 頁全部一致；證據包 341 個重算（data-overlay）。另寫寬偵測全量掃正文「單一成分／單方」說法，跟成分欄矛盾的 32 句以 `hk-lic-20261124d-*` 更正（多是「皆為單一成分」而實為複方，例 ginseng、bictegravir、valproic_acid），`hk-lic-20261117-serine-1` 同 id 重發（前版存 history）。checker 0→0。
