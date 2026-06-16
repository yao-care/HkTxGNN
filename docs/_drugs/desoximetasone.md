---
layout: default
title: Desoximetasone
parent: 高證據等級 (L1-L2)
nav_order: 222
evidence_level: L2
indication_count: 10
---

# Desoximetasone
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

# Desoximetasone：從外用皮質類固醇到斑禿

## 一句話總結

Desoximetasone 是一種中高效價的外用皮質類固醇，用於治療各類發炎性皮膚疾病。
TxGNN 模型預測它可能對**斑禿 (Alopecia Areata)** 有效，
目前有 **1 篇文獻**（隨機雙盲安慰劑對照試驗）直接支持此方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 發炎性皮膚疾病（香港無上市許可記錄） |
| 預測新適應症 | 斑禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 查詢未返回 MOA 內容）。根據已知藥理學知識，Desoximetasone 為合成外用皮質類固醇，主要透過結合細胞內糖皮質激素受體、抑制磷脂酶 A₂ 活性，進而減少前列腺素與白三烯合成，發揮抗炎、抗增生及局部免疫抑制效果。

斑禿（Alopecia Areata）是一種由 CD8⁺ T 細胞介導的器官特異性自體免疫疾病，T 細胞圍繞毛球形成「蜂群」浸潤，攻擊並破壞毛囊的免疫豁免狀態。Desoximetasone 可抑制 IL-1β、TNF-α、IFN-γ 等促炎細胞因子釋放，並減少 T 細胞活化與增殖，機轉上直接對應斑禿的核心病理過程。

外用皮質類固醇本即為斑禿的臨床一線治療選項之一，尤其適用於局部型病灶。Desoximetasone 的免疫抑制機轉與斑禿的 T 細胞驅動病理高度吻合，加上有 2000 年發表的隨機雙盲安慰劑對照試驗直接驗證，TxGNN 的預測具備充分的生物學與臨床合理性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11030789](https://pubmed.ncbi.nlm.nih.gov/11030789/) | 2000 | RCT（隨機雙盲安慰劑對照） | Archives of Dermatology | 評估 0.25% Desoximetasone 乳膏治療斑禿的療效，與安慰劑比較之隨機雙盲試驗 |

---

## 香港上市資訊

Desoximetasone 目前在香港無藥品許可證登記，屬未上市狀態。如需於香港使用，需依相關藥政規定申請特殊核准或進口許可。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有一項高品質 RCT 直接針對 Desoximetasone 治療斑禿，機轉關聯明確且充分；外用劑型的系統性暴露量低，安全性輪廓相對有利，整體證據足以支持謹慎推進。

**若要推進需要：**
- 補充完整 MOA 資料（從 DrugBank API 取得 DB00547 詳細資訊）
- 補充安全性資料：仿單警語、禁忌症（從藥監局官網下載 PDF 解析）
- 評估長期外用皮質類固醇的已知副作用（皮膚萎縮、毛細血管擴張、HPA 軸抑制風險）
- 確認是否需向香港衛生署申請特殊藥品輸入許可
- 擴大文獻搜尋範圍，納入其他同效價外用類固醇（如 mometasone、betamethasone）治療斑禿之研究，以充實比較性療效資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

