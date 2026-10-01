---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 552
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Memantine：從阿茲海默症用藥到肺高壓

## 一句話總結

Memantine 是 NMDA 受體拮抗劑，在香港已有 8 張許可證，但證據包內沒有收錄核准適應症文字。
TxGNN 預測它可能對**肺高壓 (Pulmonary Hypertension)** 有效，但**沒有任何臨床試驗**，只有 **2 篇間接文獻**，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肺高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Memantine 是 NMDA 受體拮抗劑。證據包沒有提供完整的作用機轉資料，這是目前的資料缺口。

肺高壓和 Memantine 原本作用的神經系統疾病差異很大。唯一的機轉線索是一篇 2021 年的前臨床論文。它指出麩胺酸／NMDA 受體軸可能與急性肺損傷、肺動脈高壓和糖尿病有關。不過該論文研究的是胰島素敏感性與脂質代謝，並沒有直接探討肺血管。

因此 99.54% 的高分只反映知識圖譜上的關聯，沒有任何證據顯示 Memantine 對肺高壓有效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | 前臨床／機轉研究 | Theranostics | NMDA 受體活化會調節胰島素敏感性與脂質代謝，僅提及該受體軸可能與肺動脈高壓有關 |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 藥動／安全性 | Clinical Drug Investigation | 研究的是 Memantine 的硝酸鹽衍生物 MN-08，在健康中國受試者中評估安全性與藥動學。MN-08 正在開發用於肺動脈高壓，但這不是 Memantine 本身的證據 |

## 香港上市資訊

共 8 張許可證，以下列出 5 張。證據包未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62748 | MEMANTINE ACTAVIS FILM-COATED TABLETS 10MG | TEVA PHARMACEUTICAL HONG KONG |
| HK-63963 | MEMANTINE SANDOZ TABLET 10MG | SANDOZ HONG KONG LIMITED |
| HK-62744 | ALBIX TABLETS 10MG | LSB (HK) LIMITED |
| HK-67034 | MARIXINO TABLETS 10MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-61399 | APO-MEMANTINE TAB 10MG | HIND WING CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症（供參考）

同一份資料中，另有三個預測適應症，其中偏頭痛的證據明顯強於肺高壓。

| 預測適應症 | TxGNN 分數 | 證據等級 | 重點 |
|-----------|-----------|---------|------|
| 偏頭痛 (Migraine Disorder) | 99.52% | L1 | 有 Phase 3 已完成試驗 [NCT04698525](https://clinicaltrials.gov/study/NCT04698525)，比較 Memantine 與 Valproate 預防發作型偏頭痛，但僅 33 人且未提供結果。另有 [RCT 統合分析 (PMID 33961371)](https://pubmed.ncbi.nlm.nih.gov/33961371/) 與 [系統性回顧 (PMID 34352118)](https://pubmed.ncbi.nlm.nih.gov/34352118/)，但有評論指出證據仍不足 |
| 腦幹型先兆偏頭痛 (Migraine with Brainstem Aura) | 99.41% | L4 | 沒有針對此亞型的試驗，只能從一般偏頭痛文獻間接推論 |
| 脊柱後側彎性心臟病 (Kyphoscoliotic Heart Disease) | 99.43% | L5 | 無試驗、無文獻，找不到機轉關聯 |

## 結論與下一步

**決策：Hold**

**理由：**
- 肺高壓沒有任何臨床試驗，也沒有直接文獻，只有圖譜預測分數，證據等級為 L5。
- 目前唯一與肺動脈高壓相關的臨床開發是衍生物 MN-08，不能當作 Memantine 本身的證據。

**若要推進需要：**
- 補齊 Memantine 的作用機轉資料，並找出它與肺血管病理之間的可能連結。
- 補上香港衛生署仿單的警語與禁忌症，安全性篩選才能進行。
- 先做肺高壓動物模型或機轉研究，再考慮臨床試驗。
- 若要優先投入資源，證據較完整的**偏頭痛**是更合適的研究方向，但需要有足夠檢定力的安慰劑對照試驗來確認。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

