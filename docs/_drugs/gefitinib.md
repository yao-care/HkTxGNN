---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Gefitinib：預測新適應症為牙齦纖維瘤病 (Fibromatosis, Gingival)（證據等級 L5）。原適應症：非小細胞肺癌、肺癌"
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung hilum carcinoma"]
---

# Gefitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Gefitinib：從非小細胞肺癌到牙齦纖維瘤病

## 一句話總結

Gefitinib 是一種 EGFR 酪胺酸激酶抑制劑，原本用於非小細胞肺癌（肺癌）的治療。
TxGNN 模型預測它可能對**牙齦纖維瘤病 (Fibromatosis, Gingival)** 有效，
但目前**沒有臨床試驗**和**文獻**支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、肺癌（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 牙齦纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Gefitinib 是 EGFR 酪胺酸激酶抑制劑，其在 EGFR 突變的非小細胞肺癌中的療效已被證實。

牙齦纖維瘤病的特徵是纖維母細胞增生與細胞外基質堆積。EGFR 與 TGF-β 訊號之間的交互作用，理論上可能參與這個過程，所以機轉上有可能適用。不過這個連結目前**僅屬推測**，沒有任何研究佐證。

TxGNN 的高分（0.9989）只是計算預測，不等同臨床證據。

**其他排名較前的預測（皆為 L5 或僅有極少證據）：**
- **肺纖維瘤 (Fibroma of Lung)**，分數 99.86%：良性纖維性肺腫瘤並非已知的 EGFR 驅動疾病，機轉依據薄弱。
- **VCP 相關包涵體肌病合併早發性 Paget 病 (± 額顳葉失智)**，分數 99.86%：病因為 VCP 突變，與 EGFR 抑制沒有已知連結，預測可能只反映知識圖譜的網絡關聯。
- **肺錯構瘤 (Hamartoma of Lung)**，分數 99.86%：與 HMGA 重排相關而非 EGFR，且良性病灶通常採觀察或手術切除，使用全身性激酶抑制劑的效益風險比偏低。
- **肺門癌 (Lung Hilum Carcinoma)**，分數 99.86%：本質上是現有肺癌適應症的解剖學亞型，並非真正的藥物再利用。若腫瘤帶有 EGFR 活化突變，機轉上合理。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首位預測（牙齦纖維瘤病），目前無相關文獻。

作為參考，排名第 5 的「肺門癌」有 1 篇個案報告：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22688581](https://pubmed.ncbi.nlm.nih.gov/22688581/) | 2012 | Case report | General thoracic and cardiovascular surgery | 一名 EGFR 突變的晚期肺腺癌女性患者，使用 gefitinib 後達部分緩解，後續接受補救性手術 |

這篇報告支持臨床合理性，但不足以證明在此族群的療效。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51753 | IRESSA TAB 250MG（AstraZeneca） | 錠劑 | 未載明 |
| HK-66380 | VEIASU TABLETS 250MG（Lotus） | 錠劑 | 未載明 |
| HK-66963 | GEFITINIB SANDOZ TABLETS 250MG（Sandoz） | 錠劑 | 未載明 |
| HK-67079 | GEFITINIB TABLETS 250MG（I & C） | 錠劑 | 未載明 |
| HK-68033 | GEFITINIB STADA TABLETS 250MG（STADA） | 錠劑 | 未載明 |

另有 6 張有效的單方許可證，目前共 11 張，皆為有效狀態，無已註銷者。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（EGFR 酪胺酸激酶抑制劑），非傳統細胞毒性化療 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（知識圖譜提示需留意肝臟與肺部狀況） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**：肝病、膽囊疾病、間質性肺病、肺纖維化、發炎後肺纖維化。這些來自知識圖譜的藥物—疾病關聯，並非仿單原文，須與仿單核對。
- **藥物交互作用**：共查得 100 筆，以下為已列出的主要項目。
  - 中度：
    - 抑制胃酸藥物：famotidine、ranitidine、cimetidine、nizatidine、omeprazole、esomeprazole、lansoprazole、dexlansoprazole、pantoprazole、rabeprazole
    - 抗感染藥物：clarithromycin、miconazole、clotrimazole
    - 其他：aprepitant、dexamethasone、naltrexone、troglitazone
  - 等級未知：calcitriol、glimepiride

胃酸抑制劑會改變胃內 pH 值，可能影響 gefitinib 的吸收，臨床上需特別留意。

香港仿單的警語與禁忌資料尚未取得，其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（牙齦纖維瘤病）只有模型分數，沒有臨床試驗或文獻，證據等級為 L5，機轉連結僅屬推測。
- 其餘高分預測多為良性病灶或與 EGFR 無明確關聯，不建議以全身性激酶抑制劑貿然推進。

**若要推進需要：**
- 補齊 gefitinib 作用機轉資料，並建立 EGFR/TGF-β 與牙齦纖維母細胞增生的機轉證據（細胞或動物前臨床研究）
- 取得香港仿單的警語與禁忌，完成安全性篩選
- 評估良性疾病使用 EGFR 抑制劑的效益風險比（特別是間質性肺病與肝毒性風險）
- 若要優先探索，肺門癌因屬現有適應症的亞型，可作為較務實的研究問題，需確認 EGFR 突變狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

