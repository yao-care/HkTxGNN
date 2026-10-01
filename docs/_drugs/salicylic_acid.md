---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 784
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic acid：從外用角質溶解（雞眼貼布、軟膏）到乳突性結膜炎

## 一句話總結

Salicylic acid（水楊酸）在香港以雞眼貼布、軟膏等外用產品上市，作用偏向角質溶解（此用途由產品名稱推斷，許可證未載明適應症）。
TxGNN 模型預測它可能對**乳突性結膜炎 (Papillary Conjunctivitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 乳突性結膜炎 (Papillary Conjunctivitis) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Salicylic acid 屬於水楊酸類，已知具有抗發炎活性（抑制 COX），機轉上與過敏性或發炎性結膜疾病有間接關聯。

但這個關聯相當薄弱。Salicylic acid 是角質溶解劑，對黏膜有刺激性，若用於眼部有安全疑慮。0.9988 的高分只代表模型預測，並非藥理證據。

其他排名前 10 的預測也呈現同樣問題：多數是罕見遺傳性骨骼或發育異常（如 brachyolmia、pseudoachondroplasia），找不到合理的藥理連結，推測是知識圖譜結構造成的假象。其中較有間接關聯的是酒糟性結膜炎（局部抗發炎、角質溶解作用與酒糟鼻有間接關係，但眼部組織不同、刺激風險高），以及脊椎關節病變易感性（水楊酸類是 NSAID，NSAID 是脊椎關節炎的標準症狀治療，但該適應症是遺傳易感性而非活動性疾病）。這兩者同樣沒有針對 salicylic acid 本身的試驗或文獻。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症，故不列出。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-61139 | TAWA CORN PLASTERS 32MG/STRIP | BEST UNITED MARKETING LIMITED |
| HK-59855 | MANNINGS CORN PLASTERS 50% | MANNINGS O/B THE DAIRY FARM COMPANY, LIMITED |
| HK-62936 | HC-SALICYLIC ACID OINTMENT 2%W/W | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-58293 | DECADOID CORN PLASTER 10% | MING TAI PHARMACEUTICALS COMPANY O/B SURE BRILLIANT INDUSTRIAL LIMITED |
| HK-61132 | EASTONECORN CORN PLASTERS 32MG/STRIP | BEST UNITED MARKETING LIMITED |

## 安全性考量

- **眼部使用風險**：salicylic acid 為角質溶解劑，對黏膜有刺激性，眼部暴露有刺激風險。這是模型推論的風險提示，並非仿單資料。
- **藥物交互作用**：資料庫查詢無結果。

警語與禁忌症資料缺漏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有任何臨床試驗或文獻，機轉關聯也很薄弱。
- 現有香港產品是皮膚用的貼布和軟膏，與眼部用途的安全性和劑型需求差距大。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症。
- 從 DrugBank 補充作用機轉資料。
- 系統性搜尋 salicylic acid 與結膜炎的文獻與試驗。
- 評估眼部給藥的安全性（黏膜刺激、耐受性）與劑型可行性。
- 確認給藥途徑相容性（現有產品均為皮膚外用，並無眼用劑型）。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

