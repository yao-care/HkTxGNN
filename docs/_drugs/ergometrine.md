---
layout: default
title: Ergometrine
parent: 中證據等級 (L3-L4)
nav_order: 279
evidence_level: L3
indication_count: 10
---

# Ergometrine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Ergometrine：從子宮收縮到偏頭痛（Migraine Disorder）

## 一句話總結

Ergometrine 是麥角生物鹼類子宮收縮劑，傳統用於預防與治療產後出血。TxGNN 模型預測了 10 個候選適應症，其中**偏頭痛（Migraine Disorder）**具備最強的藥理合理性，是唯一有直接臨床數據支持的候選適應症，目前有 **20 篇文獻**支持，含 3 項直接使用 ergonovine／methylergonovine 的前瞻性或回顧性臨床研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 子宮收縮、產後出血預防（Uterotonic） |
| 最佳再利用候選 | 偏頭痛（Migraine Disorder） |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

> **📌 注意**：TxGNN 評分最高的前 6 個預測（多毛症、腎性抗利尿不當症候群、先天性畸形等）均為 L5 等級，無任何臨床或文獻佐証，判斷為知識圖譜網絡傳播偽訊號，不具再利用合理性，不列為主要討論對象。

---

## 為什麼這個預測合理？

Ergometrine（ergonovine）是麥角生物鹼（ergot alkaloid）家族成員，與 ergotamine、methysergide、methylergonovine 具有密切的結構與藥理關係。雖然本 Evidence Pack 中 MOA 資料缺失（DG002），從大量歷史文獻推斷，其主要藥理機轉為 **5-HT1B/1D 受體激動**及 **α-腎上腺素受體激動**，引發平滑肌收縮與顱內血管緊縮——與 ergotamine 治療偏頭痛的核心機轉完全相同。

偏頭痛的神經血管理論認為，三叉神經激活導致顱內血管異常擴張與炎症介質（CGRP、P 物質）釋放。麥角生物鹼透過收縮擴張的顱內血管、抑制三叉神經末梢 CGRP 釋放，達到終止或預防偏頭痛的效果。Methysergide（ergometrine 的半合成衍生物）在 1960-1970 年代曾是一線偏頭痛預防藥物；methylergonovine（ergometrine 的 N-甲基衍生物）至今仍有前瞻性及回顧性臨床研究支持其對難治性偏頭痛與月經性偏頭痛的療效。

最關鍵的直接佐証來自 PMID 2759844（1989），針對 40 名月經性偏頭痛患者給予間歇性 ergonovine maleate 預防療法、6 個月追蹤顯示有效，使偏頭痛成為本次 10 個 TxGNN 預測中唯一具備**直接藥物-疾病臨床數據**的候選適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記（Ergometrine × 偏頭痛）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2759844](https://pubmed.ncbi.nlm.nih.gov/2759844/) | 1989 | 前瞻性臨床系列 | Headache | 40 名月經性偏頭痛患者接受間歇性 ergonovine maleate 預防療法，6 個月追蹤，**直接 ergometrine 臨床證據** |
| [23432443](https://pubmed.ncbi.nlm.nih.gov/23432443/) | 2013 | 回顧性世代研究 | Headache | 口服 methylergonovine（ergometrine 衍生物）用於難治性偏頭痛及叢發性頭痛預防 |
| [19895705](https://pubmed.ncbi.nlm.nih.gov/19895705/) | 2009 | 前瞻性觀察 | Head & Face Medicine | 靜脈注射 methylergonovine 用於急診嚴重偏頭痛的先導研究，顯示有效性 |
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | 回顧性評論 | Cephalalgia | Methysergide（ergometrine 半合成衍生物）的偏頭痛預防系統回顧，機轉類同 |
| [556819](https://pubmed.ncbi.nlm.nih.gov/556819/) | 1977 | 病例系列 | Neurology | 8 名頸動脈痛患者使用偏頭痛預防藥物（含麥角類）有效，支持血管性頭痛機轉 |
| [7216754](https://pubmed.ncbi.nlm.nih.gov/7216754/) | 1980 | 臨床研究 | Headache | 偏頭痛間歇預防療法長期結果，麥角類藥物療效評估 |
| [5761912](https://pubmed.ncbi.nlm.nih.gov/5761912/) | 1969 | 臨床研究 | British Medical Journal | 反覆性頭痛預防，含麥角衍生物的多藥比較 |
| [23216317](https://pubmed.ncbi.nlm.nih.gov/23216317/) | 2013 | 安全性回顧 | Headache | QT 延長、Torsade de Pointes 及冠狀動脈痙攣的偏頭痛用藥安全評估，⚠️ 重要心血管禁忌警示 |
| [6773347](https://pubmed.ncbi.nlm.nih.gov/6773347/) | 1980 | 不良事件報告 | AJR | Ergotrate（ergometrine）治療偏頭痛引發胸膜增厚的案例，⚠️ 長期使用安全性警示 |
| [13306339](https://pubmed.ncbi.nlm.nih.gov/13306339/) | 1955 | 歷史回顧 | Int Arch Allergy | 麥角療法治療偏頭痛的歷史發展，ergometrine 早期臨床應用紀錄 |

---

## 香港上市資訊

Ergometrine 在香港目前**未上市**，無藥品許可證登記。如需臨床應用，須經香港衛生署特別進口申請（Unregistered Drug Import Authorization）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

**⚠️ 來自本次 Evidence Pack 文獻的重要安全警示：**

| 安全顧慮 | 文獻依據 | 嚴重程度 |
|---------|---------|---------|
| 冠狀動脈痙攣（Prinzmetal 型變異性心絞痛） | PMID 15293589、23216317 | 高 |
| 肺動脈高壓急性加重（絕對禁忌） | PMID 26050249、41844474 | 高 |
| 腦血管病（RCVS）——腦幹型先兆偏頭痛禁忌 | PMID 10971665 | 高 |
| QT 延長 / Torsade de Pointes | PMID 23216317 | 中-高 |
| 胸膜 / 後腹膜纖維化（長期使用） | PMID 6773347 | 中 |

> 特別說明：本次 TxGNN 預測中「腦幹型先兆偏頭痛（Rank 8）」與「肺高壓（Rank 10）」均已出現反向安全証據，這些預測應解讀為**禁忌症信號**，而非治療機會。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Ergometrine 有直接臨床証據支持月經性偏頭痛的間歇性預防療法（PMID 2759844，40 例前瞻性臨床系列），機轉上與已核准的 ergotamine 完全一致；近年 methylergonovine 的多項臨床研究亦提供佐証。然而藥物在香港未上市、安全性資料缺口大，且對特定亞型偏頭痛（腦幹型先兆偏頭痛）及心肺合併症患者存在嚴重禁忌，必須嚴格篩選適用族群。

**若要推進需要：**
- 補齊 DG001（香港衛生署仿單警語/禁忌）與 DG002（DrugBank MOA）兩項資料缺口
- 建立嚴格患者排除標準：心血管疾病、高血壓、肺高壓、腦幹型先兆偏頭痛、周邊血管疾病、雷諾氏症
- 規劃香港衛生署特別進口申請路徑或新藥臨床試驗申請（IND）
- 優先定位**月經性偏頭痛**亞型（直接臨床佐証最充分，且用藥為短程間歇性，降低長期纖維化風險）
- 制訂監測計畫：心電圖（QT 間期）、血壓、肢端血液循環，長期使用需定期影像排除胸膜/後腹膜纖維化
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

