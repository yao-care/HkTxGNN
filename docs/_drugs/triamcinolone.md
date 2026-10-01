---
layout: default
title: Triamcinolone
parent: 中證據等級 (L3-L4)
nav_order: 888
evidence_level: L4
indication_count: 10
---

# Triamcinolone
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Triamcinolone：從原適應症（許可證未載明）到黏蛋白性禿髮

## 一句話總結

Triamcinolone（曲安奈德）是一種皮質類固醇，香港目前有 20 張許可證。
TxGNN 模型預測它可能對**黏蛋白性禿髮 (Alopecia Mucinosa，即毛囊黏蛋白病)** 有效，
但目前**沒有臨床試驗**，只有 **4 篇文獻**（皆為個案報告或教育性題目），且沒有任何一篇顯示使用過 triamcinolone。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 黏蛋白性禿髮 (Alopecia Mucinosa) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Triamcinolone 屬於糖皮質素類藥物，一般認為透過糖皮質素受體產生抗發炎與免疫抑制作用。

毛囊黏蛋白病是一種毛囊發炎性疾病。對局部病灶，病灶內注射或外用類固醇在機轉上合理，因此模型給出高分。

不過，目前檢索到的文獻全是個案報告或教育性題目，唯一提到的治療是 bexarotene 凝膠，並未使用 triamcinolone。證據只是間接的。0.9999 的分數是模型預測，不是臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23968145](https://pubmed.ncbi.nlm.nih.gov/23968145/) | 2014 | 個案報告 | International Journal of Dermatology | 以 bexarotene 凝膠成功治療持續性特發性毛囊黏蛋白病（非 triamcinolone） |
| [4136515](https://pubmed.ncbi.nlm.nih.gov/4136515/) | 1974 | 個案報告 | Archives of Dermatology | 黏蛋白性禿髮合併神經毛囊變化（無摘要，未見 triamcinolone 資料） |
| [14170262](https://pubmed.ncbi.nlm.nih.gov/14170262/) | 1964 | 個案報告 | Hifuka Kiyo. Acta Dermatologica | Pinkus 型黏蛋白性禿髮（毛囊黏蛋白病）一例（無摘要） |
| [9917176](https://pubmed.ncbi.nlm.nih.gov/9917176/) | 1998 | 教育性題目 | European Journal of Dermatology | 毛囊黏蛋白病的臨床測驗題（無療效資料） |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-53955 | MECOL ORABASE OINTMENT 1MG/G | WELLDONE PHARMACEUTICALS LIMITED |
| HK-63140 | KOWELL ORABASE PASTE 0.1%W/W | WELLDONE PHARMACEUTICALS LIMITED |
| HK-64378 | EURALOG PASTE 0.1% W/W | EUROPHARM LAB CO LTD |
| HK-57710 | SUNBIN MEDICINE CREAM 0.1% | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |
| HK-18543 | LECORT IN ORAL BASE 0.1% | WILCOME PHARMACEUTICAL CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測加上無關 triamcinolone 的個案報告，無任何臨床試驗，證據等級為 L4。
- 香港仿單的警語與禁忌資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症
- 補充 DrugBank 的作用機轉資料
- 針對 triamcinolone 與毛囊黏蛋白病做專題文獻搜尋，包含病灶內注射的個案或病例系列
- 確認可用劑型與給藥途徑（目前香港許可證多為外用或口腔基質製劑，是否含注射劑型待確認）

**補充：同一份預測清單中的其他候選**
- 「Quinquaud 禿髮性毛囊炎 (Folliculitis Decalvans)」有 23 位病人的回顧性研究（PMID 25277850 與 25775663 疑為同一研究重複收錄），證據等級 L3，較值得優先做全文審閱。
- 其餘候選（如 telogen effluvium、各類罕見遺傳性禿髮、類固醇抗性腎病症候群）多為僅有模型預測，部分甚至與疾病定義相衝突，建議維持 Hold。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

