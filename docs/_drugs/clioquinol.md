---
layout: default
title: Clioquinol
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 7
---

# Clioquinol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Clioquinol：從局部抗感染用藥到皮膚念珠菌症

## 一句話總結

Clioquinol（DrugBank：DB04815）是一種金屬螯合型的抗菌、抗真菌成分，香港目前有 20 張含此成分的外用許可證，但 Evidence Pack 沒有列出原適應症。
TxGNN 模型預測它可能對**皮膚念珠菌症 (Cutaneous Candidiasis)** 有效，目前**無臨床試驗**，只有數篇年代較早、且多為複方製劑的文獻，直接證據有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（許可證的核准適應症欄位皆為空） |
| 預測新適應症 | 皮膚念珠菌症 (Cutaneous Candidiasis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L3（僅有早期臨床評估，且多為複方製劑） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題，待補證據，且僅限外用） |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據一般藥理知識，Clioquinol 能螯合鋅、銅、鐵等金屬離子，具有抗真菌與抗細菌活性，因此對念珠菌有局部作用在機轉上是合理的。

值得注意的是，Clioquinol（商品名 Vioform）歷史上本來就是外用抗感染藥，所以這項預測比較像是**重新確認舊有用途**，而不是真正的新適應症。
全身性使用 Clioquinol 曾與亞急性脊髓視神經病變（SMON）相關，因此任何用途都應限於外用。

其他預測中，Majocchi 肉芽腫、毛外型與毛內型感染、深部癬（tinea profunda）都涉及毛囊或深層組織，外用藥穿透力有限，通常需要全身性治療，合理性較低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為與皮膚念珠菌症預測相關的文獻（依證據力排序）。多數文獻使用的是含 Clioquinol 的複方，或是否含 Clioquinol 尚未確認，無法單獨歸因於 Clioquinol。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | 雙盲臨床研究 | Dermatologica | 430 名患者；Locacorten-Vioform（含 Clioquinol）乳膏對合併細菌感染的皮膚病效果顯著，優於單一成分與安慰劑（針對細菌感染，非念珠菌） |
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | 隨機對照 | J Int Med Res | 154 名患者（含 67 例皮膚念珠菌症）；比較兩種類固醇加抗菌複方乳膏，其中一種含 iodochlorhydroxyquin（Clioquinol），療效相當 |
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | 臨床評估 | Curr Med Res Opin | 以 iodochlorhydroxyquin-hydrocortisone 為對照組，治療 40 例念珠菌症的有效率為 43%，試驗藥 HNA 為 95%（試驗藥並非 Clioquinol 製劑） |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | 臨床評估 | Curr Ther Res | Halcinonide 與抗真菌複方的評估；是否含 Clioquinol 未確認，無摘要 |

其他預測適應症的相關文獻如下：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33772895](https://pubmed.ncbi.nlm.nih.gov/33772895/) | 2021 | 前臨床 | Mycoses | Clioquinol 併用 ciclopirox 與 terbinafine，在皮癬菌症替代模型中評估活性與刺激性（淺部黴菌症） |
| [13521766](https://pubmed.ncbi.nlm.nih.gov/13521766/) | 1958 | 歷史臨床報告 | Antibiotic Med Clin Ther | Vioform-氫皮質酮乳膏與乳液用於淺部黴菌感染，受類固醇混雜影響 |

「頭皮或鬍鬚皮癬」檢索到的 20 篇文獻皆為關鍵字誤配（鬍鬚重建、植髮等），與 Clioquinol 無關，不列為證據，需以更精確的查詢重新檢索。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64376 | EURO-HYDROFORM CREAM | 乳膏（資料未標示） | 資料未提供 |
| HK-21173 | HYDROCORTISONE WITH CLIOQUINOL CREAM | 乳膏（資料未標示） | 資料未提供 |
| HK-53961 | TOPICAN CREAM | 乳膏（資料未標示） | 資料未提供 |
| HK-36901 | QUINOSONE CREAM | 乳膏（資料未標示） | 資料未提供 |
| HK-28056 | SUPRAL CREAM | 乳膏（資料未標示） | 資料未提供 |

（共 20 張許可證，此處列出 5 張。品名皆含 Cream，判斷為外用乳膏。）

---

## 安全性考量

- **重要風險**：全身性使用 Clioquinol 與亞急性脊髓視神經病變（SMON）相關，任何用途都應限於外用。

其餘警語、禁忌症與藥物交互作用查無資料，請參考香港衛生署核准的原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 皮膚念珠菌症在機轉上合理，且 Clioquinol 歷史上即為外用抗感染藥，但現有文獻多為含類固醇或其他成分的複方製劑，無法單獨歸因於 Clioquinol，也沒有臨床試驗。
- 安全性資料（仿單警語與禁忌）有缺口，屬於阻擋性缺口，尚無法進入安全性篩選。
- 其餘預測（Majocchi 肉芽腫、毛外／毛內型感染、深部癬）僅有模型預測，且外用穿透力不足，建議暫緩。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症
- 補查 DrugBank 的作用機轉資料
- 針對 Clioquinol 單方（或明確標示含 Clioquinol 的製劑）重新做文獻檢索，區分其與類固醇的貢獻
- 對「頭皮或鬍鬚皮癬」重做精準檢索
- 確認現有 20 張許可證的核准適應症，判斷皮膚念珠菌症是否已涵蓋，避免把既有用途誤判為新適應症
- 明確限定外用途徑，並規劃 SMON 相關風險的溝通與監測
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

