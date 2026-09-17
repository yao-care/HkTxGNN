---
layout: default
title: Neratinib
parent: 高證據等級 (L1-L2)
nav_order: 519
evidence_level: L2
indication_count: 10
---

# Neratinib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Neratinib：從 HER2 陽性乳癌到 Normal-like 乳癌分子亞型

## 一句話總結

Neratinib 是一款不可逆 pan-HER（EGFR/HER2/HER4）酪胺酸激酶抑制劑，臨床上已核准用於 HER2 陽性乳癌的輔助與轉移性治療。TxGNN 模型預測它可能對 **Normal breast-like 乳癌分子亞型**有效，目前僅有 **1 個 Phase 2 臨床試驗**、**無直接文獻**支持，證據等級偏低（L2）。值得注意的是，同一份證據包中另有 2 個乳癌相關適應症（PR 陽性、PR 陰性乳癌）證據等級達 L1，見下方「其他預測適應症一覽」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（依證據包中試驗/文獻脈絡推斷；本藥物台灣、香港均無許可證資料） |
| 預測新適應症 | Normal breast-like subtype of breast carcinoma（正常乳腺樣乳癌分子亞型） |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Research Question |

---

## 其他預測適應症一覽

此證據包為多適應症候選（TW-DB11828-multi），除主要預測外，TxGNN 同時排出以下候選，證據強弱差異大：

| Rank | 疾病 | TxGNN 分數 | 證據等級 | 決策建議 |
|------|------|-----------|---------|---------|
| 1 | Normal breast-like 乳癌亞型 | 99.68% | L2 | Research Question |
| 2 | PR 陽性乳癌 | 99.68% | L1 | Proceed with Guardrails |
| 3 | PR 陰性乳癌 | 99.67% | L1 | Proceed with Guardrails |
| 4 | Luminal A/B 乳癌 | 99.67% | L4 | Hold |
| 5 | 滑膜肉瘤 | 98.08% | L5 | Hold |
| 6 | 腱鞘巨細胞瘤 | 97.38% | L5 | Hold |
| 7 | 惡性巨細胞瘤 | 96.07% | L5 | Hold |
| 8 | 局限型腱鞘巨細胞瘤 | 95.80% | L5 | Hold |
| 9 | 纖維母細胞腫瘤 | 95.56% | L5 | Hold |
| 10 | 腎臟纖維肉瘤 | 95.53% | L5 | Hold |

Rank 2、3（PR 陽性/陰性乳癌）本質上仍是 HER2+ 乳癌族群的再確認，證據最紮實；Rank 5-10 缺乏任何臨床試驗或文獻，機轉上與 pan-HER 通路無已知關聯，屬純模型預測。

---

## 為什麼這個預測合理？

DrugBank 未提供正式 MOA 摘要（資料缺口 DG002），但依據試驗與文獻脈絡，Neratinib 是不可逆 pan-HER（EGFR/HER2/HER4）酪胺酸激酶抑制劑，已透過 ExteNET 第三期試驗（PMID 26874901）等核准用於 HER2 陽性乳癌的輔助與轉移性治療。

Normal breast-like 為 PAM50 分子亞型之一，多數呈現 HER2 低表現或陰性，與 neratinib 的主要標的（HER2/EGFR 過度表現）機轉關聯較弱，是相對薄弱的連結。

唯一支持試驗 NCT01670877 針對 HER2 non-amplified 但 HER2 突變的轉移性乳癌患者測試 neratinib 反應，顯示嘗試將 pan-HER 抑制延伸至傳統認為低表現的族群，但仍屬探索性質，尚未有第二個獨立試驗佐證，因此證據等級僅列 L2。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | 完成 | 56 | 檢測乳癌是否帶有 HER2 突變，並評估突變陽性患者對 neratinib（單用或併 fulvestrant）的治療反應 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Neratinib 目前未於香港取得藥品許可證（market_status：未上市，許可證數：0），無上市品項可列出。

---

## 細胞毒性

Neratinib 為抗腫瘤藥物（pan-HER 酪胺酸激酶抑制劑），列出以下資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（不可逆 pan-HER 酪胺酸激酶抑制劑，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

註：本證據包缺乏 TFDA 仿單警語/禁忌資料（資料缺口 DG001，屬 Blocking 等級），故毒性相關細項無法引用具體數據。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Research Question**

**理由：**
- 主預測適應症（Normal breast-like 乳癌亞型）僅有 1 個 Phase 2 試驗、無文獻佐證，機轉關聯性也相對薄弱，證據等級 L2，尚不足以支持積極推進。
- 同一批預測中的 PR 陽性/陰性乳癌適應症證據等級達 L1（多個 Phase 2/3 試驗＋RCT 文獻如 ExteNET、NALA），且本質上與 neratinib 既有核心用途（HER2+ 乳癌）高度重疊，建議優先評估這兩個候選而非本適應症。

**若要推進需要：**
- 補齊 TFDA/藥監局仿單警語與禁忌症資料（DG001，Blocking，需先解決才能進入 S1 安全性初評）
- 取得正式 DrugBank MOA 摘要以強化機轉關聯性分析（DG002）
- 針對 Normal-like 亞型尋找第二個獨立試驗以提升證據等級至 L1
- 若優先推進 PR 陽性/陰性乳癌適應症，需補充 route_compatibility（劑型/給藥途徑）與 similarity_to_original 分析（目前皆為 pending）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

