---
layout: default
title: Pregabalin
parent: 高證據等級 (L1-L2)
nav_order: 413
evidence_level: L2
indication_count: 5
---

# Pregabalin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Pregabalin：從神經痛/癲癇輔助治療到偏頭痛預防（研究假說）

## 一句話總結

Pregabalin 原本核准用於神經痛、癲癇輔助治療、纖維肌痛與廣泛性焦慮症（GAD）等適應症。
TxGNN 模型針對此藥物共產生 5 個高分預測適應症，但證據品質差異極大——其中證據等級最高、最具臨床意義的是**偏頭痛預防 (Migraine Disorder)**，目前有 **3 個臨床試驗**和 **19 篇文獻**支持；其餘 4 個候選（肌腱炎、肌炎相關疾病）則僅有模型統計關聯分數，缺乏機轉或臨床佐證，建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 神經痛、癲癇輔助治療、纖維肌痛、廣泛性焦慮症（GAD）※香港未上市，無本地許可證核准文字可查 |
| 預測新適應症（最具證據力） | 偏頭痛預防 (Migraine Disorder) |
| TxGNN 預測分數 | 99.47%（rank 9255） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question（列為研究假說，尚不足以進入 Go/Proceed 階段） |

> 註：TxGNN 對此藥物另預測出肌腱炎（rank 1，L4）、肌肉纖維化（rank 2，L5）、特發性肉芽腫性肌炎（rank 3，L5）、包涵體肌炎（rank 4，L5）等 4 個候選，但經證據審視後機轉關聯薄弱，詳見下方「其他預測適應症」章節。

---

## 為什麼這個預測合理？

目前 DrugBank 未提供結構化的 Pregabalin 作用機轉資料（Data Gap），但依據文獻與 evidence pack 中的機轉分析：Pregabalin 是 **α2δ-1 電位依賴性鈣離子通道調節劑**，可降低神經末梢麩胺酸、P 物質等興奮性神經傳導物質的釋放。

偏頭痛的病理生理與「中樞敏感化（central sensitization）」及「皮質過度興奮性（cortical hyperexcitability）」有關，這與 Pregabalin 原核准的神經痛、癲癇輔助治療機轉高度重疊。事實上，其他已用於偏頭痛預防的抗癲癇藥物（如 topiramate、valproate、gabapentin）皆透過類似的鈣/鈉離子通道調節或 GABA 能路徑發揮預防效果，因此 Pregabalin 用於偏頭痛預防屬於「同類別藥物效應（class-effect）延伸假說」，機轉合理性中等偏高。

需特別注意的是，偏頭痛預防**並非** Pregabalin 目前核准的適應症，且動物實驗（皮質擴散抑制，cortical spreading depression）雖支持機轉假說，但關鍵的 Phase 3 RCT（NCT00447369）已撤回（WITHDRAWN），未能提供完整療效數據，因此仍屬研究假說階段，而非確立療效。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00447369](https://clinicaltrials.gov/study/NCT00447369) | Phase 3 | 已撤回 (Withdrawn) | 70 | 唯一直接針對「Pregabalin 用於偏頭痛預防」設計的樞紐試驗（vs. sodium valproate 之隨機交叉試驗），但因撤回而無可用療效數據 |
| [NCT02747940](https://clinicaltrials.gov/study/NCT02747940) | Phase 4 | 已完成 | 200 | 慢性疼痛（含慢性偏頭痛、纖維肌痛）之神經影像/生物標記觀察性研究，非介入性療效試驗，僅提供機轉層級資訊 |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | 邀請登記中 | 3300 | 神經科實務品質改善計畫（EMR-based pragmatic trial），涵蓋 10 種常見神經疾病，非專門評估 Pregabalin 療效 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-Analysis | JAMA Network Open | 兒童偏頭痛預防用藥之網絡統合分析，比較各類預防性藥物療效與安全性 |
| [37637787](https://pubmed.ncbi.nlm.nih.gov/37637787/) | 2023 | RCT | Iranian J Child Neurology | Pregabalin 與 Sodium Valproate 於兒童偏頭痛預防之隨機對照試驗比較 |
| [26024701](https://pubmed.ncbi.nlm.nih.gov/26024701/) | 2015 | RCT | Acta Medica Iranica | Propranolol 與 Pregabalin 於兒童偏頭痛預防之隨機對照試驗，評估療效、安全性與耐受性 |
| [19935409](https://pubmed.ncbi.nlm.nih.gov/19935409/) | 2010 | 開放性研究 | Clinical Neuropharmacology | Pregabalin 用於慢性偏頭痛預防治療之開放性研究 |
| [21479703](https://pubmed.ncbi.nlm.nih.gov/21479703/) | 2011 | 開放性追蹤研究 | J Headache Pain | Pregabalin 作為偏頭痛預防治療之 3 個月追蹤研究，評估療效與耐受性 |
| [25669613](https://pubmed.ncbi.nlm.nih.gov/25669613/) | 2015 | 臨床機轉研究 | Int J Clin Pharmacol Ther | Pregabalin 對偏頭痛患者中樞敏感化（allodynia）之影響 |
| [30880369](https://pubmed.ncbi.nlm.nih.gov/30880369/) | 2019 | Review | Curr Treat Options Neurol | 抗癲癇藥物於偏頭痛預防治療之現況回顧，含 Pregabalin 定位 |
| [23797675](https://pubmed.ncbi.nlm.nih.gov/23797675/) | 2013 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | Gabapentin 或 Pregabalin 用於成人陣發性偏頭痛預防之系統性回顧 |
| [17691980](https://pubmed.ncbi.nlm.nih.gov/17691980/) | 2007 | Review | CNS Neurol Disord Drug Targets | GABA 能藥物用於偏頭痛治療之機轉綜述 |
| [28223480](https://pubmed.ncbi.nlm.nih.gov/28223480/) | 2017 | 動物實驗（活體影像） | PNAS | Pregabalin 抑制皮質擴散抑制（cortical spreading depression）並阻斷其向皮質下結構傳播，支持偏頭痛預防之機轉假說 |

---

## 其他預測適應症（證據薄弱，建議 Hold）

以下 4 個候選雖 TxGNN 分數同樣高達 99%+，但經證據審視均缺乏臨床或機轉佐證，**均建議 Hold**：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 主要問題 |
|------|-----------|-----------|---------|---------|---------|
| 1 | 肌腱炎 (Tendinitis) | 99.71% | L4 | S0 | 文獻多為「肌腱手術後止痛」而非治療肌腱炎本身，機轉上 Pregabalin 無抗發炎/組織修復作用；TxGNN 高分可能反映「疼痛」語意關聯而非疾病特異性訊號 |
| 2 | 肌肉纖維化 (Myositis Fibrosa) | 99.71% | L5 | S0 | 無任何臨床試驗或文獻支持，純屬圖譜統計關聯 |
| 3 | 特發性肉芽腫性肌炎 | 99.71% | L5 | S0 | 屬自體免疫/肉芽腫性疾病，Pregabalin 無免疫調節機轉，需人工確認是否為疾病本體命名重疊之誤判 |
| 4 | 包涵體肌炎 (Inclusion Body Myositis) | 99.52% | L5 | S0 | 退化合併發炎性肌病，目前無有效疾病修飾療法，Pregabalin 至多緩解伴隨疼痛，對疾病本身無作用機轉 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 目前無法取得香港仿單警語、禁忌症與藥物交互作用資料（DrugBank DDI 查詢無結果）。此為 **Blocking 等級資料缺口**，在補齊仿單資料前無法進行 S1 安全性初評。

---

## 結論與下一步

**決策：Research Question（列為研究假說，暫不進入 Go/Proceed 決策）**

**理由：**
- 偏頭痛預防具備機轉合理性與部分臨床證據（1 個 Cochrane 回顧、多篇 RCT/開放性研究），但關鍵樞紐試驗（NCT00447369）已撤回，證據等級僅達 L2，尚不足以支持積極推進；
- 其餘 4 個高分候選（肌腱炎、肌炎相關疾病）經審視後機轉關聯薄弱，應予以 Hold，避免資源錯置。

**若要推進需要：**
- 取得 TFDA/香港衛生署仿單 PDF 並解析警語與禁忌症，以完成 S1 安全性初評（目前為 Blocking 資料缺口）
- 查詢 DrugBank API 取得完整作用機轉（MOA）資料，強化機轉關聯性分析
- 若欲推進偏頭痛適應症，建議尋找是否有替代或後續的 Phase 3 RCT（NCT00447369 之後續或同類設計試驗）
- 針對「肌腱炎」候選，建議人工複核 TxGNN 訓練資料中是否存在「疼痛」語意混淆造成的偽陽性關聯
- 建立完整藥物交互作用（DDI）資料庫查詢結果，目前為 not_found 狀態
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

