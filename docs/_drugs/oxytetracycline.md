---
layout: default
title: Oxytetracycline
parent: 僅模型預測 (L5)
nav_order: 550
evidence_level: L5
indication_count: 5
---

# Oxytetracycline
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

# Oxytetracycline：從抗菌治療到慢性鼻竇炎

## 一句話總結

Oxytetracycline 是四環黴素（Tetracycline）類廣效抗生素成分之一，本次資料集中未查得其已核准的原始適應症紀錄。TxGNN 模型預測它可能對**慢性鼻竇炎 (Chronic Rhinosinusitis)** 有效，預測分數高達 **99.61%**，但目前**查無任何臨床試驗登記，也無文獻佐證**，屬於純模型預測（L5），且藥物本身尚未上市，安全性資料亦有缺口。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無公開許可證資料可供查證 |
| 預測新適應症 | 慢性鼻竇炎 (Chronic Rhinosinusitis) |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L5 |
| 上市狀態 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Oxytetracycline 詳細的作用機轉（MOA）資料。根據已知的藥物類別資訊，Oxytetracycline 屬於四環黴素類抗生素，同類藥物（如 doxycycline）除抗菌作用外，還具有抑制基質金屬蛋白酶（MMP）與抗發炎的特性，臨床上曾被用作慢性鼻竇炎的輔助治療，因此機轉上具備一定合理性。

不過，這個推論主要建立在「同類藥物」的類比之上，並非 Oxytetracycline 本身直接的實證資料。本資料集中查無任何以 Oxytetracycline 治療慢性鼻竇炎的臨床試驗或文獻，預測分數雖高，但目前仍完全依賴 TxGNN 模型的知識圖譜推論，尚待實證支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 安全性考量

安全性資訊請參考原廠仿單。

> 需特別注意：TFDA 仿單警語與禁忌症資料屬於**阻斷性（Blocking）資料缺口**（DG001），在取得此資料前無法進入 S1 安全性初評階段。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但決策階段僅為 S0，五個候選適應症皆無臨床試驗或文獻支持，證據等級均為 L5。
- 藥物尚未上市（0 張許可證），且仿單警語/禁忌資料為阻斷性缺口，無法進行基本安全性評估。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌症資料（DG001，Blocking，來源：TFDA 官網仿單 PDF）
- 補充 DrugBank 作用機轉（MOA）資料（DG002）
- 針對慢性鼻竇炎主動蒐集 Oxytetracycline（或同類 tetracycline）相關臨床試驗與文獻
- 確認藥物在目標市場的上市狀態與許可證資訊

---

*附註：本資料集另列出 4 個同屬 L5、Hold 狀態的候選適應症（chronic ethmoidal sinusitis、paranasal sinus neoplasm、punctate epithelial keratoconjunctivitis、postinfectious vasculitis），其中 paranasal sinus neoplasm 因與 Oxytetracycline 已知藥理無直接關聯，需留意是否為知識圖譜雜訊；punctate epithelial keratoconjunctivitis 因四環黴素眼用製劑有傳統抗菌適應症基礎，機轉合理性相對較高，可留待後續資料補齊後一併評估。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

