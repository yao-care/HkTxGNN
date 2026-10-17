---
layout: default
title: Triptorelin
parent: 僅模型預測 (L5)
nav_order: 912
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Triptorelin：預測新適應症為多毛症 (Hypertrichosis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "TRIPTORELIN"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Triptorelin
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

# Triptorelin：從（原適應症未載明）到多毛症（Hypertrichosis）

## 一句話總結

Triptorelin 是一種 GnRH（促性腺激素釋放素）促效劑，在香港已有 5 張有效許可證，但資料中未載明核准適應症。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇個案報告**，且該報告並未顯示 triptorelin 能治療多毛症。這項預測目前只是模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證未提供核准適應症文字） |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5（僅模型預測；唯一文獻為個案報告，不支持療效） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Triptorelin 屬於 GnRH 促效劑，會抑制腦下垂體－性腺軸，降低性腺的雄性素分泌。

多毛症與一般認知的「多毛（hirsutism）」不同，傳統上並非由雄性素驅動，因此 triptorelin 與多毛症之間只有間接關聯。

唯一檢索到的文獻（PMID 41822646）是一名接受睪固酮阻斷治療的跨性別女性，因 ciclosporin 而出現全身性多毛症。報告將多毛症歸因於 ciclosporin，而非荷爾蒙治療；她同時使用 estradiol 與 triptorelin，這只說明雄性素抑制下仍可能發生多毛症，**並不表示 triptorelin 能改善多毛症**。0.99997 的高分是模型預測，不應視為臨床支持。

其餘 4 項預測（Ambras 型先天性全身多毛症、牙/牙周畸形症候群、Dandy-Walker 畸形相關症候群、遺傳性毛幹異常）皆屬發育性或遺傳性結構缺陷，GnRH 促效劑沒有已知的機轉可以矯正，且均無臨床試驗與文獻，推測是知識圖譜中網絡鄰近關係所造成。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | 個案報告 | Cureus | 25 歲跨性別女性（重度斑塊型乾癬）使用 ciclosporin 後出現全身性多毛症，當時同時服用 estradiol 與 triptorelin；多毛症歸因於 ciclosporin，非 triptorelin 的療效證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51941 | DIPHERELINE PR FOR INJ 11.25MG | 未載明 | 未載明 |
| HK-47655 | DIPHERELINE PR FOR INJ 3.75MG | 未載明 | 未載明 |
| HK-36917 | DECAPEPTYL 0.1MG INJ SC | 未載明 | 未載明 |
| HK-33730 | DECAPEPTYL-CR FOR INJ 3.75MG | 未載明 | 未載明 |
| HK-62788 | DIPHERELINE P.R. POWDER AND SOLVENT FOR SUSPENSION FOR INJECTION 22.5MG | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病關聯，非仿單內容）：高血壓、腎臟疾病、膿輸尿管（pyoureter）、肝臟疾病、膽囊疾病、高血糖、糖尿病、糖尿病酮酸中毒、肥胖、單基因肥胖、泌尿道阻塞、脊髓疾病。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 重度（Major）：Dolasetron
  - 中度（Moderate）：Acarbose、Metformin、Pioglitazone、Glimepiride、Chlorpropamide、Alogliptin、Saxagliptin、Canagliflozin、Dapagliflozin、Empagliflozin、Albiglutide、Dulaglutide、Famotidine、Clarithromycin、Palonosetron、Loperamide、Bisacodyl 等。多數為降血糖藥，使用時需留意血糖控制。

香港仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一的文獻是個案報告，且未顯示 triptorelin 對多毛症有療效；無臨床試驗，機轉上也僅有間接關聯。高 TxGNN 分數只是模型預測。
- 另外 4 項預測為先天性或遺傳性結構缺陷，沒有合理的機轉依據。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，並補齊香港核准適應症資料
- 取得並解析香港仿單的警語與禁忌，完成安全性篩選
- 進行系統性文獻回顧，確認 GnRH 促效劑與多毛症之間是否有直接證據
- 若仍有意探索，先以機轉研究或小規模觀察性研究驗證，再考慮臨床試驗
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

