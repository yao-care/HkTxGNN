---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant：從化療誘發性噁心嘔吐到腎源性不適當抗利尿症候群

## 一句話總結

Aprepitant（DB00673）是選擇性 NK1（神經激肽-1）受體拮抗劑，國際上核准用於預防化療誘發性噁心嘔吐（CINV）及術後噁心嘔吐（PONV），但目前在香港尚未取得上市許可。
TxGNN 模型預測它最可能對**腎源性不適當抗利尿症候群（Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD）**有效，預測分數達 99.97%。
然而，目前**無臨床試驗**、**無直接文獻**支持此適應症，整體證據等級為 L5（僅模型預測）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 化療誘發性噁心嘔吐（CINV）/ 術後噁心嘔吐（PONV）（國際核准；香港未上市） |
| 預測新適應症 | 腎源性不適當抗利尿症候群（Nephrogenic Syndrome of Inappropriate Antidiuresis） |
| TxGNN 預測分數 | 99.97%（排名第 986） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Aprepitant 的核心作用機轉為選擇性拮抗 NK1 受體，阻斷神經傳導物質 Substance P（SP）的結合，進而抑制中樞孤束核與周邊迷走神經的嘔吐反射訊號。由於 NK1 受體廣泛分布於中樞與周邊組織，包括腎臟集合管，此一廣泛分布是 TxGNN 模型預測多種非傳統適應症的機轉基礎。

腎源性不適當抗利尿症候群（NSIAD）由 *AVPR2*（V2 血管加壓素受體）基因的功能增益型突變（多為 R137C/L/H）引起，導致 V2R 在無 ADH 刺激下持續性活化，引發腎小管不受調控地重吸收水分，臨床呈現慢性或反覆發作的低血鈉血症。Substance P 透過 NK1 受體可能在腎臟集合管中調節 V2R 的下游 cAMP 信號通路；理論上 NK1 拮抗或可減少 V2R 的組成性活化，從而減輕水分滯留。

然而，上述機轉假說目前仍屬高度推測階段。無前臨床動物模型、無體外細胞實驗、亦無任何臨床觀察報告直接驗證 aprepitant 對 NSIAD 的療效或安全性。本批次評估所有 10 個預測適應症中，NSIAD（rank 1）、蜘蛛膜下腔出血（rank 9）與肺高壓（rank 3）具有相對較清晰的 NK1/SP 機轉關聯，其餘多屬結構性發育異常，與 NK1 通路無合理關聯。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻（針對 Aprepitant × NSIAD 組合，搜尋結果為零）。

---

## 香港上市資訊

Aprepitant 目前在香港尚**未取得衛生署藥物許可證**，無相關許可證資料可查。

> **備註**：Aprepitant 在國際市場以品牌名 **Emend®**（Merck）上市，劑型包括口服膠囊（40 mg / 80 mg / 125 mg）及靜脈注射前驅藥 fosaprepitant（Ivemend®），核准適應症為化療誘發性噁心嘔吐（CINV）預防及術後噁心嘔吐（PONV）預防。如需引進香港，需另行評估本地申請途徑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 本 Evidence Pack 中的香港仿單警語、禁忌症及藥物交互作用資料均缺失（Data Gap）。已知 Aprepitant 在國際使用上涉及 CYP3A4 代謝交互作用，在取得完整安全性資料前，不建議進行臨床決策。

---

## 所有預測適應症總覽

以下為本次 Evidence Pack 全部 10 個 TxGNN 預測適應症評估概覽：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 機轉關聯性評估 | 建議 |
|------|------|-----------|---------|--------------|------|
| 1 | 腎源性不適當抗利尿症候群（NSIAD） | 99.97% | L5 | 中度（NK1 調控 V2R 訊號，推測性） | Hold |
| 2 | 多毛症（Hypertrichosis） | 99.91% | L5 | 低（NK1 抑制毛髮生長理論未被驗證；多數多毛症為雄激素依賴性） | Hold |
| 3 | 肺動脈高壓（Pulmonary Hypertension） | 99.90% | L5 | 中度（SP/NK1 對肺血管雙向調控，療效方向不確定） | Hold |
| 4 | 痲瘋病（Leprosy） | 99.90% | L5 | 低（NK1 調節巨噬細胞極化屬高度推測，感染性疾病無臨床探索） | Hold |
| 5 | Ambras 型先天性全身多毛症 | 99.87% | L5 | 極低（遺傳性結構異常，與 NK1 通路無已知關聯） | Hold |
| 6 | 含牙/牙周成分之畸形症候群 | 99.86% | L5 | 極低（文獻均為牙周病一般治療研究，無一涉及 aprepitant） | Hold |
| 7 | 脊柱側彎性心臟病（Kyphoscoliotic Heart Disease） | 99.86% | L5 | 無（力學性結構問題，與 NK1 拮抗無機轉關聯） | Hold |
| 8 | Dandy-Walker 畸形症候群 | 99.86% | L5 | 無（先天性神經發育結構缺陷，藥物無法干預既成結構異常） | Hold |
| 9 | 蜘蛛膜下腔出血（SAH）⭐ | 99.85% | L5 | 較強（SP/NK1 參與 SAH 後神經源性水腫與血管痙攣；本批次機轉最強者） | Hold |
| 10 | 遺傳性毛幹結構異常 | 99.85% | L5 | 無（角蛋白基因突變性結構缺陷，NK1 拮抗無修復機轉） | Hold |

> ⭐ **最具機轉潛力**：蜘蛛膜下腔出血（SAH, rank 9）在本批次中具有相對最清晰的 NK1 機轉基礎，可優先進行文獻深挖與前臨床研究評估。

---

## 結論與下一步

**決策：Hold**

**理由：**
Aprepitant 在本次評估的所有 10 個預測適應症中，均未發現直接支持性臨床試驗或文獻證據，全數停留於 L5 模型預測層級；加上香港尚未上市、仿單安全性資料缺失，不具備進入下一階段評估的條件。

**若要推進需要：**
- 補充 Aprepitant 的完整作用機轉資料（DrugBank MOA、CYP 代謝途徑、蛋白結合率）
- 下載並解析原廠仿單（Emend® Package Insert）以填補警語與禁忌資料缺口
- 優先針對機轉最強的 **蜘蛛膜下腔出血（SAH）** 進行 PubMed 深入文獻搜尋（關鍵字：substance P + subarachnoid hemorrhage, NK1 antagonist + cerebral vasospasm）
- 評估 NSIAD 的孤兒藥地位，確認是否有患者族群可支持小型概念驗證試驗
- 若考慮香港市場進入，需評估向衛生署申請藥物注冊的可行性與時程

---

> **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選需經過嚴格的臨床驗證方可應用於患者。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

