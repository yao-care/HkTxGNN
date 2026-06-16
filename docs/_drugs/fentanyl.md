---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fentanyl：從疼痛管理到腎性抗利尿不當症候群

## 一句話總結

Fentanyl 是強效合成阿片類鎮痛藥，廣泛應用於手術麻醉與急慢性疼痛管理。
TxGNN 模型預測它可能對**腎性抗利尿不當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，預測分數高達 99.46%，
然而目前**無任何臨床試驗或文獻**支持此方向，屬純計算預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 疼痛管理（強效合成阿片類鎮痛藥，手術麻醉及慢性疼痛） |
| 預測新適應症 | 腎性抗利尿不當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 預測分數 | 99.46% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fentanyl 是強效 μ-opioid receptor agonist，透過與中樞及周邊神經系統的 μ 受體結合，抑制疼痛信號傳導，達到強效鎮痛效果。

**預測的理論基礎**：NSIAD 由 AVPR2（V2 vasopressin receptor）功能增益型突變引起，導致受體在無 AVP（精氨酸加壓素）刺激下持續活化，造成持續性水分滯留與低血鈉。Fentanyl 作為 μ-opioid receptor agonist，理論上可透過下視丘-垂體軸抑制 AVP 釋放（opioid 誘發 SIADH 的已知機轉），但此效果的作用層次是降低 AVP 分泌量，而非修正 NSIAD 中受體本身的構成性活化缺陷。

**機轉關聯的根本侷限**：兩者病理機制層次不同——opioid 影響的是 ligand 層面（AVP 分泌），NSIAD 的核心問題卻在於受體側的 constitutive activation，不依賴 ligand。TxGNN 高分（0.9946）最可能源自知識圖譜中 vasopressin pathway 的間接網路關聯（opioid → AVP → V2R），屬計算推論，而非具有直接生物學支撐的機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港目前無 Fentanyl 相關藥品許可證登記（共 0 張）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **重要提示**：Fentanyl 為高度成癮性管制藥物，在多數醫療體系中屬第一級管制麻醉藥品。其呼吸抑制（即使在治療劑量下）、高度成癮性及過量致死風險（治療窗窄，約為嗎啡的 50–100 倍效力），在任何新適應症開發規劃中均必須列為首要安全性障礙，需於方案設計初期即予以正式評估。

---

## 附：第二預測適應症摘要

| 項目 | 內容 |
|------|------|
| 預測適應症 | 妥瑞症 (Tourette Syndrome) |
| TxGNN 分數 | 99.05% |
| 證據等級 | L5 |
| 臨床試驗數 | 0 |
| 文獻數 | 0 |
| 建議決策 | Hold |

**機轉簡評**：妥瑞症主要涉及紋狀體多巴胺能過度活化（cortico-striato-thalamo-cortical circuit 失調）。雖然內源性鴉片系統可調節紋狀體多巴胺釋放，且 1980–90 年代曾有探索性研究使用 opioid antagonist（naloxone、naltrexone）治療妥瑞症，但 opioid agonist 在此適應症幾乎無文獻支持。Fentanyl 的成癮性與呼吸抑制風險在神經精神適應症中構成嚴重的安全性障礙，不宜優先推進。

---

## 結論與下一步

**決策：Hold**

**理由：**
兩個預測適應症（NSIAD、妥瑞症）均為 L5 純計算預測，臨床試驗數與文獻數皆為零，且機轉連結為間接的知識圖譜網路關聯，而非直接生物學機轉。加之 Fentanyl 的高度成癮性、嚴格管制地位及呼吸抑制風險，在缺乏任何外部驗證證據的情況下，不具備推進再利用研究的基礎。

**若要推進需要：**
- 補充完整 MOA 資料（DrugBank API 查詢 DB00813）
- 搜尋 μ-opioid receptor 與 AVP 系統交互作用的基礎研究文獻
- 評估管制藥物用於新適應症的法規許可路徑（香港藥劑業及毒藥管理局）
- 若 NSIAD 方向有機轉興趣，考慮先以 non-addictive opioid analogue 或其他 AVP pathway 干預藥物作為替代評估對象
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

