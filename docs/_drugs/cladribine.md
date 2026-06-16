---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 7
---

# Cladribine
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

# Cladribine：從血液腫瘤到傍腦膜胚胎型橫紋肌肉瘤

## 一句話總結

Cladribine 是一種嘌呤核苷類似物，原用於治療血液惡性腫瘤（如毛細胞白血病）。
TxGNN 模型預測它可能對**傍腦膜胚胎型橫紋肌肉瘤 (parameningeal embryonal rhabdomyosarcoma)** 有效，
但目前**無任何臨床試驗**或**文獻**直接支持此預測，屬純模型推斷結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料集未收錄（嘌呤核苷類似物，臨床主要用於血液惡性腫瘤） |
| 預測新適應症 | 傍腦膜胚胎型橫紋肌肉瘤 (parameningeal embryonal rhabdomyosarcoma) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據本 Evidence Pack 各適應症的機轉描述，Cladribine 作為嘌呤核苷類似物，透過抑制 DNA 合成及誘導細胞凋亡發揮抗腫瘤效果。其選擇性毒殺特性主要針對淋巴球型細胞，原因在於這類細胞的 deoxycytidine kinase（DCK）與 5'-核苷酸酶（5'-NT）比值較高，使藥物在細胞內磷酸化積累，從而產生細胞毒殺效果。

傍腦膜胚胎型橫紋肌肉瘤屬間葉組織來源的惡性腫瘤，為橫紋肌肉瘤中的高風險亞型。其腫瘤細胞的 DCK/5'-NT 比值尚未有文獻量化，Cladribine 在此類腫瘤中的選擇性作用基礎薄弱，機轉連結主要停留在「一般性細胞毒性」的層次，而非針對 RMS 生物學的特定作用。

目前 RMS 標準治療為 VAC 方案（vincristine、actinomycin-D、cyclophosphamide）± 放射治療，Cladribine 在此疾病脈絡下缺乏機轉優先性支撐。TxGNN 高分預測（99.77%）主要反映知識圖譜的拓撲關聯性，而非直接的藥物–疾病機轉證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤核苷類似物） |
| 骨髓抑制風險 | 高（重度且持久的骨髓抑制為主要劑量限制毒性，包括嗜中性白血球減少、血小板減少、貧血） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝功能（ALT／AST）、腎功能（Creatinine）、感染徵象（因免疫抑制風險高） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；免疫抑制期間須預防機會性感染（包括 PCP 預防用藥評估） |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 TxGNN 模型預測（L5），缺乏任何臨床試驗或文獻支持 Cladribine 用於傍腦膜胚胎型橫紋肌肉瘤；藥物的淋巴球靶向特性與 RMS 細胞生物學機轉不符，且 Cladribine 在香港未上市，藥物可及性需額外評估。

**若要推進需要：**
- 確認 Cladribine 在 RMS 細胞株中的 DCK 表達量及體外細胞敏感性（in vitro）數據
- 收集難治性／復發 RMS 現有救援治療文獻，評估 Cladribine 是否有探索性研究空間（參考 Rank 6 研究假說方向）
- 補充 Cladribine 完整安全性資料（原廠仿單警語、禁忌症、藥物交互作用）
- 評估香港藥物可及性：目前未上市，需透過臨床試驗申請或特殊進口途徑取得
- 補充藥物作用機轉（MOA）詳細資料，以強化機轉關聯性分析
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

