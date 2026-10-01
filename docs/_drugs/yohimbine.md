---
layout: default
title: Yohimbine
parent: 僅模型預測 (L5)
nav_order: 932
evidence_level: L5
indication_count: 10
---

# Yohimbine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Yohimbine：從（原適應症未載明）到偏頭痛

## 一句話總結

Yohimbine 是一種 α2 腎上腺素受體拮抗劑，在香港已有 1 張上市許可證，但許可證資料沒有載明原適應症。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效。
目前**沒有臨床試驗**，只有 **20 篇間接文獻**，內容多為血清素、兒茶酚胺與其他藥物（如 reserpine）的研究，**沒有任何一篇直接測試 yohimbine**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4（僅有前臨床與機轉相關研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。從文獻推論，Yohimbine 是 α2 腎上腺素受體拮抗劑，會增加交感神經的去甲腎上腺素釋放。

偏頭痛的病理與血清素、兒茶酚胺失衡有關。大鼠研究也顯示，α2 腎上腺素調控會影響皮質擴散性抑制（cortical spreading depression，偏頭痛先兆的生理基礎）。這是模型預測的主要機轉線索。

不過這條線索有明顯限制：

- 現有文獻幾乎都是間接證據，例如 reserpine、血清素或其他腎上腺素藥物。
- 作用方向不確定，α2 拮抗反而可能加重症狀。
- 有數篇文獻描述 reserpine 會誘發頭痛，這不支持療效。
- 99.94% 的分數只是模型預測，不等於療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下 10 篇為與偏頭痛機轉最相關者。資料中沒有 RCT，也沒有任何一篇直接以 yohimbine 為研究對象。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26908](https://pubmed.ncbi.nlm.nih.gov/26908/) | 1978 | 回顧／假說 | Postgraduate Medical Journal | 重新檢視偏頭痛的自律神經學說：去甲腎上腺素釋放增加導致顱內血管收縮 |
| [5634006](https://pubmed.ncbi.nlm.nih.gov/5634006/) | 1967 | 回顧 | Transactions of the American Neurological Association | 探討血清素與偏頭痛的關係 |
| [171561](https://pubmed.ncbi.nlm.nih.gov/171561/) | 1975 | 回顧（未正式分類） | MMW Munchener Medizinische Wochenschrift | 偏頭痛發作涉及血漿激肽、血清素、組織胺等體液介質，並討論酪胺的角色 |
| [934534](https://pubmed.ncbi.nlm.nih.gov/934534/) | 1976 | 臨床研究（未正式分類） | Minerva Medica | 以 reserpine 預防偏頭痛，300 位重度患者的結果達統計顯著；藥物是 reserpine，不是 yohimbine |
| [468534](https://pubmed.ncbi.nlm.nih.gov/468534/) | 1979 | 臨床觀察 | Headache | 研究 reserpine 引發的頭痛與偏頭痛患者的泌乳素（PRL）釋放 |
| [1270244](https://pubmed.ncbi.nlm.nih.gov/1270244/) | 1976 | 臨床觀察 | Headache | 探討偏頭痛、酪胺與血中血清素的關聯 |
| [15829916](https://pubmed.ncbi.nlm.nih.gov/15829916/) | 2005 | 前臨床（大鼠） | J Cereb Blood Flow Metab | 腎上腺素促效劑與拮抗劑都會影響皮質擴散性抑制的傳播，可能與偏頭痛預防有關 |
| [29856967](https://pubmed.ncbi.nlm.nih.gov/29856967/) | 2018 | 前臨床／人體生理 | Experimental Neurology | 壓力透過 α2 腎上腺素與糖皮質素受體調節皮質興奮性（擴散性抑制） |
| [17103145](https://pubmed.ncbi.nlm.nih.gov/17103145/) | 2006 | 前臨床（豬） | Naunyn-Schmiedeberg's Arch Pharmacol | 比較現有與潛在抗偏頭痛藥對豬腦膜動脈的作用，涉及血清素與 α 腎上腺素受體 |
| [15778266](https://pubmed.ncbi.nlm.nih.gov/15778266/) | 2005 | 前臨床 | J Pharmacol Exp Ther | 多巴胺在三叉神經血管痛覺模型中的作用 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44766 | PMS-YOHIMBINE TAB 6MG | 未登載 | 未登載 |

製造商為 TRENTON-BOMA LTD。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻皆為間接證據，沒有任何研究直接測試 yohimbine 治療偏頭痛。
- α2 拮抗的作用方向可能與療效相反，而香港仿單的警語與禁忌症尚未取得，無法進入安全性篩選。

排名前 10 的其他預測也都是 Hold，證據等級為 L4 或 L5。其中注意力不足過動症（ADHD）的預測，機轉方向很可能與治療效果相反。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症（目前阻擋進度的缺口）。
- 補齊 DrugBank 的作用機轉資料。
- 先釐清 α2 拮抗對偏頭痛的作用方向，例如在擴散性抑制或三叉神經血管模型中直接測試 yohimbine。
- 前臨床結果支持後，再評估是否設計小型臨床研究。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

