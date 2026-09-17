---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Iodixanol
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

# Iodixanol：從醫學影像顯影劑到 Osteoarthritis Susceptibility（骨關節炎易感性）

## 一句話總結

Iodixanol 是非離子型碘化顯影劑，用於電腦斷層（CT）與血管攝影等醫學影像檢查，本身並無治療性適應症。
TxGNN 模型預測其可能與**骨關節炎易感性（Osteoarthritis Susceptibility）**相關，
但目前**無任何臨床試驗、無任何文獻**支持此預測；同批前 10 名預測也呈現同樣的證據真空模式，判斷為知識圖譜嵌入偏誤（KG artifact）而非真實再利用機會。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無治療性適應症（醫學影像用非離子型碘顯影劑） |
| 預測新適應症 | Osteoarthritis Susceptibility（骨關節炎易感性） |
| TxGNN 預測分數 | 99.16%（rank 13,447） |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Iodixanol 詳細的作用機轉資料。根據已知資訊，Iodixanol 是一種非離子型、等滲透壓（iso-osmolar）碘化 X 光顯影劑，其唯一已知功能是提供 X 光吸收對比度以利影像判讀，**不具備任何藥理性治療標的**，因此無法從機轉角度支持其對骨關節炎易感性或任何疾病產生治療效果。

TxGNN 對此候選給出高達 99.16% 的分數，但檢索結果顯示**完全沒有**對應的臨床試驗或文獻證據（`evidence.clinical_trials` 與 `evidence.literature` 皆為空）。對照同批次第 2 名預測「osteoarthritis」（一般骨關節炎，非「易感性」子項），雖然檢索到 7 篇文獻，但內容全部是將 iodixanol 作為 CT 顯影劑或擴散示蹤劑，用來**研究**軟骨結構、物質轉運或奈米顆粒擴散影像技術，屬於影像研究工具用途，並非治療性介入證據。

這個模式在前 10 名預測中重複出現：第 3～10 名（rheumatoid arthritis、hemoglobinopathy、以及多個罕見骨骼發育不良症候群）的機轉論述皆明確指出「無機轉基礎」「僅為顯影劑偶然共現」。最合理的解釋是，Iodixanol 在知識圖譜中因大量「顯影劑－關節／骨骼影像研究」共現關係，與骨骼、軟骨相關節點在嵌入空間中距離過近，導致 TxGNN 產生高分但無臨床意義的預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻（針對 Osteoarthritis Susceptibility 本身）。

補充說明：檢索到的 7 篇文獻是對應同批次第 2 名「osteoarthritis」（非易感性子項），均為顯影劑影像方法學研究，非治療性證據，故不計入本適應症的正式文獻證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | 基礎科學（物質轉運） | Journal of Biomechanics | 以 iodixanol 作為中性擴散示蹤劑，研究軟骨與軟骨下骨界面的通透性 |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | 影像方法學 | Annals of Biomedical Engineering | 光子計數 CT 雙顯影劑評估關節軟骨健康的方法學研究 |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | 影像方法學 | Annals of Biomedical Engineering | 奈米顆粒擴散影像評估軟骨功能 |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | 有限元素模型 | Journal of Biomechanics | 軟骨－軟骨下骨介面中性溶質轉運的有限元素模擬 |

---

## 香港上市資訊

Iodixanol 目前**未於香港上市**，無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語與禁忌症資料尚未取得，列為 Blocking 等級資料缺口 DG001，需優先補齊才能進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症（Osteoarthritis Susceptibility）完全沒有臨床試驗或文獻支持，證據等級僅 L5。
- Iodixanol 為顯影劑而非治療藥物，缺乏可解釋此類疾病關聯的藥理機轉；前 10 名預測整體呈現「高分但零實證」的一致模式，較可能是 KG 嵌入偏誤而非真實再利用信號。

**若要推進需要：**
- 補齊作用機轉（MOA）資料（DG002, High）
- 取得 TFDA 仿單警語與禁忌症（DG001, Blocking），此為進入 S1 安全性初評的前提
- 若後續要重新評估，建議針對「osteoarthritis susceptibility」與「osteoarthritis」進行疾病本體去重複檢查，避免同一疾病的不同節點重複計分
- 目前不建議投入額外資源於此候選藥物之再利用開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

