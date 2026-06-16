---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 5
---

# Haloperidol
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

以下是根據 Evidence Pack 生成的藥物再利用評估報告：

---

# Haloperidol：從精神科用藥到先天性岩藻糖基化障礙

## 一句話總結

Haloperidol 是第一代典型抗精神病藥物，以 D2 多巴胺受體拮抗為核心藥理機轉，同時兼具 D1、5-HT2A、α-adrenergic 及 H1 受體拮抗活性。
TxGNN 模型預測它可能對**先天性岩藻糖基化障礙（Congenital Disorder of Glycosylation with Defective Fucosylation）**有效，
但目前**無任何臨床試驗或文獻**支持此方向，且機轉分析顯示缺乏直接藥理連結。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未收錄（香港許可證資料庫無對應記錄） |
| 預測新適應症 | 先天性岩藻糖基化障礙 (Congenital Disorder of Glycosylation with Defective Fucosylation) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**此預測的機轉連結目前缺乏直接支持，需謹慎解讀。**

Haloperidol 的主要藥理作用為阻斷 D2 多巴胺受體，並兼具 D1、5-HT2A、α-adrenergic 及 H1 受體拮抗活性，屬第一代典型抗精神病藥物（First-generation antipsychotic）。其在精神科的臨床應用以正性症狀控制（幻覺、妄想）為主。然而本 Evidence Pack 中作用機轉資料（MOA）標註為資料缺口，建議從 DrugBank 補充完整機轉描述。

先天性岩藻糖基化障礙（CDG type IIc）由 *SLC35C1* 基因突變所致，造成 GDP-岩藻糖無法正常轉運至高基氏體，導致細胞表面醣蛋白岩藻糖基化異常，臨床表現包括智能障礙、復發性感染及白血球黏附缺陷。

目前**無任何已知機轉**能將 D2 受體拮抗連結至岩藻糖轉運路徑或 GDP-fucose 代謝。Evidence Pack 中的機轉分析明確指出：TxGNN 高分推測來源於知識圖譜中遠端共病或間接蛋白交互作用的統計關聯，而非直接藥理連結，亦無任何生物標誌假說或細胞模型支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **附加注意**：本次評估的 5 個 TxGNN 預測適應症中，有部分存在潛在致害風險：
> - **視網膜退化症**（Rank 2）：Haloperidol 長期使用已知可能引發視網膜色素上皮病變，多巴胺訊號減少可能加重光適應缺陷，機轉方向與治療目標相反。
> - **X 連鎖近視**（Rank 4）：多巴胺（透過 D1 受體）能抑制眼軸延長，而 D2 拮抗劑理論上可能促進眼軸延長，加重近視。
> - **夏科馬里牙病 CMT1G**（Rank 5）：部分抗精神病藥物具周邊神經毒性，可能加重 CMT 患者症狀。

---

## 結論與下一步

**決策：Hold**

**理由：**
五個 TxGNN 預測適應症均為 L5（僅模型預測，無任何臨床試驗或文獻支持），且機轉分析逐一顯示無合理藥理連結；部分預測（視網膜退化症、X 連鎖近視、CMT1G）甚至存在潛在加重病情的理論風險，不建議在未建立合理機轉假說前推進。

| 預測排名 | 適應症 | 機轉評估 | 建議 |
|---------|--------|---------|------|
| 1 | 先天性岩藻糖基化障礙 | 無連結 | Hold |
| 2 | 視網膜退化症 | 可能有害 | Hold |
| 3 | 水腦症 | 結構性缺損，不適合藥物干預 | Hold |
| 4 | X 連鎖近視 | 機轉方向相反 | Hold |
| 5 | CMT1G 脫髓鞘神經病 | 無連結，潛在神經毒性 | Hold |

**若要推進需要：**
- 補充香港藥監局核准適應症、警語及禁忌資料（Data Gap DG001）
- 從 DrugBank API 補充完整作用機轉說明（Data Gap DG002）
- 委託罕見疾病代謝專家評估 GDP-fucose 路徑與多巴胺系統的可能交互假說
- 若有意探索視網膜或近視方向，需先行排除 Haloperidol 本身的眼毒性風險，並改以多巴胺促進劑為研究方向
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

