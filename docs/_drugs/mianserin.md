---
layout: default
title: Mianserin
parent: 僅模型預測 (L5)
nav_order: 581
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Mianserin：預測新適應症為良性嬰兒陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy)（證據等級 L5）。原適應症：單極性憂鬱症、內因性憂鬱症、重度憂鬱症、焦慮症"
monitor_inn: "Mianserin"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "Ohdo syndrome and variants"]
---

# Mianserin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Mianserin：從憂鬱症到良性嬰兒陣發性斜頸

## 一句話總結

Mianserin 是一種四環類抗憂鬱藥，原本用於單極性憂鬱症、內因性憂鬱症、重度憂鬱症與焦慮症。
TxGNN 模型預測它可能對**良性嬰兒陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy)** 有效，但目前**沒有臨床試驗，也沒有相關文獻**支持，僅有模型預測分數。

> 說明：在 7 個預測適應症中，排名第 1 的預測證據最弱。證據相對較多的是神經症 (neurotic disorder)、憂鬱相關病症（見結論）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 單極性憂鬱症、內因性憂鬱症、重度憂鬱症、焦慮症（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 良性嬰兒陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy) |
| TxGNN 預測分數 | 99.49% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。從藥理資料來看，Mianserin 可與多種血清素受體（5-HT1B、2A、2B、2C、6、7）、α1 腎上腺素受體及正腎上腺素轉運體 (NET) 作用，但這些資料不足以解釋它為何對新適應症有效。

良性嬰兒陣發性斜頸是罕見、通常可自行緩解的兒童疾病，常與 CACNA1A 相關的離子通道異常有關。目前沒有已知機轉可將 Mianserin 與此疾病連結。此預測僅來自模型分數，無實證支持。

此外，此疾病的患者為嬰幼兒，而 Mianserin 在兒童的使用經驗有限，會帶來額外的安全疑慮。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55706 | VICK-MIANSERIN TAB 30MG | 未載明 | 未載明 |
| HK-55705 | VICK-MIANSERIN TAB 10MG | 未載明 | 未載明 |
| HK-58331 | MIANSERIN 10 TAB 10MG | 未載明 | 未載明 |
| HK-58332 | MIANSERIN 30 TAB 30MG | 未載明 | 未載明 |

## 安全性考量

- **藥物交互作用**：資料庫中共查得 11 筆，但內容均為 Mianserin 與受體或轉運體的藥理作用（如 5-HT 受體、α1 腎上腺素受體、LPA1 受體、NET），並非與其他藥物的交互作用，無法用於臨床用藥判斷。

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數支持，沒有臨床試驗或文獻，也找不到合理的作用機轉。
- 患者為嬰幼兒且疾病多可自行緩解，風險效益比不利。

**若要推進需要：**
- 釐清 Mianserin 與 CACNA1A 或相關離子通道病變之間是否有機轉關聯
- 取得作用機轉 (MOA) 資料
- 取得香港仿單的警語與禁忌症，並評估兒童族群的安全性
- 取得任何 Mianserin 用於此疾病的臨床或前臨床證據

**其他預測適應症的補充觀察：**

| 預測適應症 | 分數 | 證據等級 | 建議 | 重點 |
|-----------|------|---------|------|------|
| 精神官能症 (neurotic disorder) | 99.02% | L3 | Research Question | 有 Mianserin 與 clomipramine、imipramine 的對照研究，但年代較久，且此診斷分類已過時；為此組中證據最強者 |
| 輕鬱症 (dysthymic disorder) | 99.45% | L4 | Research Question | 僅有抗憂鬱藥類別層級的統合分析，無 Mianserin 專屬證據 |
| 憂鬱性精神官能症 (neurotic depression) | 99.16% | L4 | Research Question | 多為一般抗憂鬱藥文獻，另有少數 Mianserin 研究；與既有適應症高度重疊 |
| 憂鬱症／憂鬱型 (melancholia) | 99.17% | L4 | Research Question | 與既有適應症重疊，較可能是術語重疊而非真正的新用途 |
| 懼曠症 (agoraphobia) | 99.40% | L4 | Hold | 僅有 MAO-A 抑制劑的文獻，並非 Mianserin 證據 |
| Ohdo 症候群及其變異型 | 99.23% | L5 | Hold | 僅有模型預測，無任何研究或機轉依據 |

若要優先投入研究資源，建議從證據較多的神經症與憂鬱相關病症開始，而非排名第 1 的預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

