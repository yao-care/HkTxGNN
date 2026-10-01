---
layout: default
title: Brompheniramine
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 2
---

# Brompheniramine
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

# Brompheniramine：從抗組織胺（原適應症未載明）到過敏性蕁麻疹

## 一句話總結

Brompheniramine 是第一代 H1 抗組織胺藥，香港有 20 張許可證，但許可證資料未載明原適應症。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效，另預測**寒冷性蕁麻疹 (Cold Urticaria)**。
目前**沒有臨床試驗和文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

其他預測：寒冷性蕁麻疹 (Cold Urticaria)，分數 99.55%，證據等級 L5，建議 Hold。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Brompheniramine 屬於第一代烷基胺類 H1 受體拮抗劑。依一般藥理知識，蕁麻疹的風團與紅暈由肥大細胞釋放組織胺所引起，阻斷 H1 受體在機轉上合理。這個推論來自一般藥理學，並非本次提供的資料。

過敏性蕁麻疹和寒冷性蕁麻疹都涉及肥大細胞的組織胺釋放。TxGNN 分數很高（約 99.9%），但可能主要反映知識圖譜中「抗組織胺藥類別」與蕁麻疹的關聯，而非這個藥物本身的證據。

H1 抗組織胺本來就是蕁麻疹的標準治療，因此這可能只是藥物類別已有的標示用途，不算真正的老藥新用。需對照產品仿單確認。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

共 20 張許可證，以下列出 5 張（許可證資料未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-49258 | PUKAMIN TAB 4MG | HITPHARM PHARMACEUTICAL CO LTD |
| HK-22814 | BROMITON TAB 4MG | CHRISTO PHARM LTD |
| HK-55190 | BROMPHENIRAMINE TAB 4MG (JEN SHENG) | LANWAY LIMITED |
| HK-21866 | BROMITON SYRUP 2MG/5ML | CHRISTO PHARM LTD |
| HK-52673 | BRONCOMINE TAB 4MG | VAST RESOURCES PHARMACEUTICAL LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症都只有模型預測（L5），沒有任何試驗或文獻。
- 香港仿單的警語與禁忌資料也還沒取得，無法進入安全性篩選。

**若要推進需要：**
- 從香港衛生署下載並解析仿單，確認核准適應症是否已涵蓋蕁麻疹。若已涵蓋，這只是既有用途，不是新用途。
- 從 DrugBank 補齊作用機轉資料。
- 搜尋 brompheniramine 用於過敏性及寒冷性蕁麻疹的臨床試驗與文獻。
- 評估第一代抗組織胺的抗膽鹼與中樞神經副作用，並補做較完整的藥物交互作用查詢，目前查詢結果為零筆，可能不完整。

*本報告結果僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

