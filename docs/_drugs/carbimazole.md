---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 3
---

# Carbimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Carbimazole：從甲狀腺機能亢進到甲狀腺激素受體 β 突變引起的甲狀腺激素抵抗

## 一句話總結

Carbimazole 是一種 thionamide 類抗甲狀腺藥物，廣泛用於甲狀腺機能亢進（如 Graves 氏病）的治療，但目前在香港尚未取得任何藥品許可證。
TxGNN 模型最高分預測它可能對**甲狀腺激素受體 β 突變引起的甲狀腺激素抵抗 (RTH-β)** 有效，
但目前僅有 **1 篇文獻**，且該文獻記錄的是誤診情境，臨床合理性存疑。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲狀腺機能亢進（香港未登記，依藥理認知） |
| 預測新適應症（TxGNN #1） | 甲狀腺激素受體 β 突變引起的甲狀腺激素抵抗 |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Carbimazole 是 thionamide 類抗甲狀腺藥物的代表性成員，在體內迅速轉換為活性代謝物 methimazole，透過抑制甲狀腺過氧化酶（TPO）阻斷甲狀腺素（T4/T3）的碘化生物合成，是歐洲及亞太地區最廣泛使用的抗甲狀腺藥物之一。

甲狀腺激素受體 β 突變（THRβ mutation）引起的甲狀腺激素抵抗（RTH-β）是一種罕見的遺傳性疾病，其特徵為血中游離 T4 升高、TSH 未被抑制（甚至偏高）——外觀上酷似甲狀腺機能亢進，但病因完全不同：問題在於靶器官對激素不敏感，而非激素分泌過量。TxGNN 的預測邏輯可能基於「高 T4 水平」這一表面特徵，將 Carbimazole 的降甲狀腺素效果映射至 RTH-β。

然而，此預測在機轉上存在根本矛盾：RTH-β 患者的高甲狀腺素屬於「代償性」反應，身體必須維持更高濃度才能達到正常的細胞激素效應。若以 Carbimazole 降低甲狀腺素合成，反而會加重組織激素不足，可能導致臨床惡化。唯一相關文獻（PMID 24165508）正是記錄了一位 RTH-β 患者被誤診為甲亢、間歇性接受 Carbimazole 治療長達十年而無效的案例，直接印證此預測路徑的謬誤。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case Report | BMJ Case Reports | RTH-β 患者因 fT4 持續升高（25–35.7 pmol/L）且 TSH 未被抑制（6.78–22.1 mIU/L），被誤診為甲亢並間歇性使用 Carbimazole 長達 10 年，療效不佳；最終確診為 THRβ 突變，說明此情境下 Carbimazole 無效且診斷意義相悖 |

---

## 香港上市資訊

Carbimazole 在香港目前未取得任何藥品許可證，無上市記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
唯一相關文獻呈現的是 Carbimazole 在 RTH-β 情境下的誤診使用案例，而非療效佐證；機轉分析亦顯示降低甲狀腺素合成對 RTH-β 患者可能有害。此預測的生物合理性不足，不建議進一步推進。

**若要推進需要：**
- 建立 THRβ 突變動物模型或細胞株，驗證 Carbimazole 在此情境的實際效果
- 評估 TxGNN 是否因「高 T4」的表面特徵產生假陽性預測，而非真正的機轉相關性
- 系統性回顧抗甲狀腺藥物用於 RTH-β 的所有文獻，確認是否存在特殊有效亞型

---

---

## 附加預測適應症

本 Evidence Pack 涵蓋三項預測適應症，以下呈現第 2、3 名候選之評估。

---

### 預測 #2：新生兒甲狀腺毒症 (Neonatal Thyrotoxicosis)

*TxGNN 分數：99.41% | 證據等級：L3 | 建議決策：Proceed with Guardrails*

#### 為什麼這個預測合理？

新生兒甲狀腺毒症主因為母體 TRAb（TSH 受體刺激抗體）經胎盤傳遞，持續活化新生兒甲狀腺的 TSH 受體，驅動 T4/T3 過量合成。Carbimazole 透過抑制 TPO 直接阻斷激素生物合成，作用路徑明確且有雙重給藥策略：（1）孕期給予母體，藥物穿越胎盤保護胎兒；（2）出生後直接給予新生兒。此為機轉清晰、有數十年臨床使用記錄的成熟適應症，雖無 RCT，但屬全球公認的 well-established practice。

#### 臨床試驗證據

目前無相關臨床試驗登記（此屬罕見疾病，難以進行 RCT）。

#### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24251220](https://pubmed.ncbi.nlm.nih.gov/24251220/) | 2013 | Narrative Review | Indian J Endocrinol Metab | 新生兒甲狀腺毒症發生率、病因（母體 TSI 經胎盤傳遞）及 Carbimazole 治療方案，死亡率 12–20% |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | 妊娠期甲亢管理指引，詳述 Carbimazole 與 PTU 的適用時機、劑量及胎兒/新生兒監測要求 |
| [1971773](https://pubmed.ncbi.nlm.nih.gov/1971773/) | 1990 | Observational Clinical Study | Clin Endocrinol | 44 名 Graves 病孕婦及 48 名嬰兒的 TBII、甲狀腺功能與抗甲狀腺藥物劑量關聯分析 |
| [7523202](https://pubmed.ncbi.nlm.nih.gov/7523202/) | 1994 | Retrospective Cohort | Eur J Obstet Gynecol | 32 例妊娠合併甲亢，Carbimazole 與 PTU 均用於控制甲狀腺毒症，收錄母嬰結局完整資料 |
| [11298090](https://pubmed.ncbi.nlm.nih.gov/11298090/) | 2001 | Case Series | Clin Endocrinol | 早產兒先天性甲狀腺毒症病例系列，高 TBII 指數預測不良新生兒結局，死亡率達 25% |
| [41191399](https://pubmed.ncbi.nlm.nih.gov/41191399/) | 2025 | Case Report | Endocrinol Diabetes Metab Case Rep | 新生兒甲狀腺毒症合併嚴重高鈣血症，Carbimazole 治療後甲狀腺功能及血鈣均正常化 |
| [29494342](https://pubmed.ncbi.nlm.nih.gov/29494342/) | 2018 | Case Report | J Pediatr Endocrinol Metab | 自體免疫甲狀腺功能低下症母親所生嬰兒，因 TRAb 引發嚴重甲亢，Carbimazole 治療有效 |
| [27747714](https://pubmed.ncbi.nlm.nih.gov/27747714/) | 2015 | Case Report | Drug Safety Case Reports | 新生兒甲狀腺毒症合併高血壓，Carbimazole 合用 Amlodipine 致嚴重低血壓（提示新生兒 DDI 風險） |
| [12124735](https://pubmed.ncbi.nlm.nih.gov/12124735/) | 2002 | Case Report | Am J Med Genet | 第 4 例母體 Carbimazole 暴露與後鼻孔閉鎖相關案例（第 35–38 天最高劑量期），提示胚胎毒性風險 |
| [23320593](https://pubmed.ncbi.nlm.nih.gov/23320593/) | 2013 | Case Report | J Paediatr Child Health | 母體甲狀腺毒症合併胎兒甲狀腺腫，宮內 levothyroxine 注射治療胎兒甲低，產後以 Carbimazole 治療新生兒甲亢 |

#### 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
文獻支持 Carbimazole 用於新生兒甲狀腺毒症的臨床實踐已逾半世紀，全球內分泌學會指引均認可此適應症。雖無 RCT，但觀察性資料及個案報告提供充分的真實世界佐證。

**若要推進需要：**
- 確認香港藥劑師可取得、調配並監測新生兒口服 Carbimazole 劑型（低劑量製備，如 500 µg 每 8 小時）
- 參照 ETA／ATA 指引制定母嬰監測計畫（TBII 指數、新生兒 TSH/fT4、血球計數）
- 注意 Carbimazole 胎盤透過性及可能的胚胎毒性（妊娠早期後鼻孔閉鎖風險），一般建議妊娠前三月優先使用 PTU

---

### 預測 #3：高甲狀腺素血症 (Hyperthyroxinemia)

*TxGNN 分數：99.21% | 證據等級：L4 | 建議決策：Research Question*

#### 為什麼這個預測合理？

Hyperthyroxinemia 是一個異質性症候群，Carbimazole 的適用性高度依賴病因：

- **真性甲亢型**（Graves 氏病、毒性結節、TSHoma、碘胺酮誘發）→ Carbimazole 的 TPO 抑制有效，此為其核心適應症
- **結合蛋白異常型**（家族性白蛋白異常高甲狀腺素血症，FDH）→ 游離 T4 實際正常，Carbimazole 無效且可能有害
- **暫時自限型**（妊娠劇吐相關、外傷後）→ 通常自限性消退，不需抗甲狀腺治療

TxGNN 預測的「Hyperthyroxinemia」作為一個整體診斷，無法直接對應 Carbimazole 的最佳適用亞型，需要病因分層後才能判斷。

#### 臨床試驗證據

目前無相關臨床試驗登記。

#### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8024995](https://pubmed.ncbi.nlm.nih.gov/8024995/) | 1994 | Case Series | Br J Clin Pract | 妊娠劇吐合併甲亢 2 例，強調 Carbimazole 適用於真性 Graves 型，暫時型不需治療，需鑑別診斷 |
| [3923304](https://pubmed.ncbi.nlm.nih.gov/3923304/) | 1985 | Clinical Review | Med J Aust | 碘胺酮誘發甲狀腺毒症合併高甲狀腺素，Carbimazole 反應欠佳，提示特殊病因需不同處置策略 |
| [3709386](https://pubmed.ncbi.nlm.nih.gov/3709386/) | 1986 | Review | Drugs | 老年甲狀腺疾病（含甲亢）的診斷挑戰，包括「冷漠型甲亢」及 Carbimazole 治療注意事項 |
| [24847468](https://pubmed.ncbi.nlm.nih.gov/24847468/) | 2014 | Case Report | Eur Thyroid J | TSHoma 合併 Graves 病共存致高甲狀腺素血症，Carbimazole 初步控制後病情轉變，提示罕見病因的複雜性 |
| [32854689](https://pubmed.ncbi.nlm.nih.gov/32854689/) | 2020 | Case Report | BMC Endocr Disord | Graves 病後出現 probable TSHoma，Carbimazole 初步有效，但後期復發需重新評估病因 |
| [3708869](https://pubmed.ncbi.nlm.nih.gov/3708869/) | 1986 | Clinical Study | Clin Endocrinol | FDH（白蛋白異常高甲狀腺素血症）機轉研究，游離 T4 實際正常，明確說明此亞型無需抗甲狀腺治療 |
| [3985431](https://pubmed.ncbi.nlm.nih.gov/3985431/) | 1985 | Case Report | Ann Fr Anesth Reanim | 外傷後高甲狀腺素血症，最終確診為真性甲亢並以 Carbimazole 治療，突顯病因鑑別的必要性 |

#### 結論與下一步

**決策：Research Question**

**理由：**
Hyperthyroxinemia 作為一個診斷類別，其內在異質性使得 Carbimazole 的療效無法一概而論。在真性甲亢亞型中 Carbimazole 有效，但其他亞型無效甚至有害，此預測需進一步病因分層研究才有臨床價值。

**若要推進需要：**
- 依病因亞型（真性甲亢 vs. FDH vs. 暫時性）分層分析文獻療效資料
- 確認 TxGNN 預測是否已考慮亞型分類，或僅依整體「高 T4」特徵做出預測
- 設計前瞻性登錄研究，追蹤不同病因的 Hyperthyroxinemia 患者對 Carbimazole 的治療反應
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

