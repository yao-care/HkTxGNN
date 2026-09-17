---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 5
---

# Levofloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Levofloxacin：從細菌感染到點狀角膜結膜炎

## 一句話總結

Levofloxacin 是氟喹諾酮類（fluoroquinolone）廣效抗生素，原本用於治療細菌感染。
TxGNN 模型預測它可能對**點狀角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，
目前**無臨床試驗登記**，僅有 **1 篇相關文獻**（且非直接療效研究），證據非常有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（Evidence Pack 未提供 Levofloxacin 於香港的核准適應症文字） |
| 預測新適應症 | 點狀角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.92%（排名 2177） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Levofloxacin 詳細的作用機轉資料（Evidence Pack 標記為 Data Gap）。根據公開藥理學知識，Levofloxacin 屬於氟喹諾酮類抗生素，透過抑制細菌 DNA 迴旋酶（DNA gyrase）與拓樸異構酶 IV 發揮殺菌作用，臨床上廣泛用於呼吸道、泌尿道等細菌感染的治療，且已有眼用製劑（如 levofloxacin 眼藥水）用於治療細菌性結膜炎。

點狀角膜結膜炎在部分病因（如細菌性合併感染）上與 Levofloxacin 的抗菌機轉有潛在關聯性，這可能是 TxGNN 模型給出高分預測的原因。但需注意，Evidence Pack 中唯一相關的文獻（PMID 30055152）討論的是**微孢子蟲（microsporidial）**感染引起的角膜結膜炎爆發事件，屬於病原體流行病學報告，並非 Levofloxacin 治療該疾病的直接療效證據，機轉關聯性仍待進一步驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | 疫情報告（分類待定） | American Journal of Ophthalmology | 台灣游泳池水污染導致微孢子蟲性角膜結膜炎群聚感染事件，未涉及 Levofloxacin 療效評估 |

> 註：此文獻與 Levofloxacin 治療該適應症的直接關聯性尚未確認（分類欄位標示為 pending）。

## 安全性考量

安全性資訊請參考原廠仿單。（Evidence Pack 標記 TFDA/香港仿單警語與禁忌症資料為 Blocking 等級 Data Gap，無法完成安全性初評）

## 結論與下一步

**決策：Hold**

**理由：**
- 該適應症目前僅有模型預測分數支持，唯一文獻並非直接療效證據，且無任何臨床試驗佐證，證據等級僅達 L5。
- Levofloxacin 於香港未上市（0 張許可證），且仿單警語/禁忌症資料缺失（Blocking 等級），無法進行安全性初評（S1）。

**若要推進需要：**
- 取得 TFDA/香港藥品仿單並解析警語與禁忌症（DG001，Blocking）
- 補充 Levofloxacin 詳細作用機轉資料（DG002，High）
- 針對點狀角膜結膜炎進行文獻檢索，尋找直接療效相關研究（如病例報告、體外抗菌活性研究）
- 確認 Levofloxacin 眼用劑型的可及性與適用途徑
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

