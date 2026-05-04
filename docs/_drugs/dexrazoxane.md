---
layout: default
title: Dexrazoxane
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Dexrazoxane
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

# Dexrazoxane：從化療心臟保護到硬化性膽管炎

## 一句話總結

Dexrazoxane 是一種鐵螯合劑，原本用於預防蒽環類化療（如 Doxorubicin）所致的心臟毒性（心肌病變）。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，
目前**無臨床試驗、無直接文獻**支持這個方向，預測尚屬純模型推斷。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 化療心臟保護（蒽環類誘發心臟毒性預防）※非香港許可資料，依藥理學通用知識填入 |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Dexrazoxane 在體內代謝為 ICRF-198，後者具備強力鐵螯合能力，可阻斷 Fenton 反應（Fe²⁺ + H₂O₂ → •OH），從而減少活性氧（ROS）對組織的氧化損傷。這是其保護心肌免受蒽環類藥物毒性的核心機轉。

原發性硬化性膽管炎（PSC）的病理特徵為膽管周圍進行性纖維化與炎症。理論上，局部氧化壓力參與膽管上皮損傷，鐵螯合作用若能降低膽管細胞的 ROS 負荷，或許可減緩纖維化進程。

然而，PSC 的**主要病理驅動力**是膽汁酸毒性與免疫介導纖維化（T 細胞異常活化、TGF-β 通路），而非鐵依賴性氧化損傷。此外，Dexrazoxane 靜脈給藥後在膽道組織的濃度分佈與有效性完全未知。整體而言，此預測的機轉連結**極弱**，屬高度推測性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Dexrazoxane 目前**未在香港上市**，無任何藥品許可證記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測為純模型推斷（L5），無任何臨床試驗或文獻支持 Dexrazoxane 用於硬化性膽管炎。
PSC 的核心病理機制（免疫纖維化、膽汁酸毒性）與 Dexrazoxane 的鐵螯合作用機轉缺乏直接連結，生物合理性極弱。加上藥物未在香港上市、安全性資料缺口（DG001/DG002）尚未填補，目前不具備推進條件。

**📎 補充說明：本批次中更值得關注的候選**

在本次 Evidence Pack 的 10 個預測中，**第 10 名「膀胱炎 (Cystitis, L4)」**具備遠高於第 1 名的生物合理性：

- 環磷醯胺代謝物丙烯醛 → 誘發膀胱尿路上皮 Ferroptosis（鐵依賴性細胞死亡）
- Dexrazoxane → 螯合游離鐵 → 阻斷 Fenton 反應 → 理論上保護膀胱上皮
- 現行標準預防（Mesna）為硫醇類清除劑，鐵螯合途徑屬機轉**互補**而非重複
- 有間接機轉文獻支持（PMID [37690746](https://pubmed.ncbi.nlm.nih.gov/37690746/)、[10193684](https://pubmed.ncbi.nlm.nih.gov/10193684/)、[7811398](https://pubmed.ncbi.nlm.nih.gov/7811398/)）

建議優先針對**化療誘發出血性膀胱炎**這一方向設計前臨床實驗，而非硬化性膽管炎。

**若要推進（以膀胱炎方向為例）需要：**
- 取得 Dexrazoxane 完整 MOA 與毒性資料（填補 DG002）
- 查閱 TFDA / EMA / FDA 仿單警語與禁忌（填補 DG001）
- 設計動物模型（CYP 誘發 HC 大鼠模型）驗證 Dexrazoxane 膀胱保護效果
- 評估 Dexrazoxane 與 Mesna 聯合使用的安全性與協同性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

