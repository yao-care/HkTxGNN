---
layout: default
title: Tamsulosin
parent: 僅模型預測 (L5)
nav_order: 834
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin：從良性攝護腺肥大到 Ambras 型先天性全身多毛症

## 一句話總結

Tamsulosin 是 α1 腎上腺素受體拮抗劑，在證據包中的原適應症為良性攝護腺肥大 (BPH)。
TxGNN 模型預測它可能對 **Ambras 型先天性全身多毛症 (Ambras type hypertrichosis universalis congenita)** 有效。
目前**沒有臨床試驗和文獻**支持，這是純模型預測，建議暫緩 (Hold)。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 良性攝護腺肥大（香港許可證資料未載明適應症文字，此處依證據包中的藥理描述） |
| 預測新適應症 | Ambras 型先天性全身多毛症 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 預測分數 | 99.996% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。已知 Tamsulosin 是用於 BPH 的 α1A/1D 腎上腺素受體拮抗劑。

Ambras 症候群是罕見的先天性疾病，與 8q22 染色體重組影響 TRPS1 調控有關。α1 受體阻斷與毛髮生長調控之間沒有已知的關聯，**目前找不到合理的藥理機轉**。

這個高分較可能來自知識圖譜中的鄰近關係（與毛髮表型相關的節點相近），而不是真正的藥理依據。因此分數雖高，不能當作療效證據。

**其他預測的情況：** 前 10 名預測（包括多毛症、毛幹異常、少毛症、斑禿、禿髮、腦幹先兆偏頭痛等）全部是 L5，沒有臨床試驗。
- 第 3 名「伴有牙齒/牙周成分的畸形症候群」有 20 篇文獻，但內容都是一般牙周炎，沒有提到 tamsulosin，只是疾病關鍵字比對。
- 第 9 名「禿髮」的 2 篇文獻，一篇談 finasteride（另一類藥物），一篇談 BPH 患者的瞼板腺，都不支持 tamsulosin 的療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Tamsulosin 在香港共有 14 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55161 | TAMSULO SUSTAINED-RELEASE CAP 0.2MG | LAFARGE CO., LIMITED |
| HK-65304 | PROSTAM PROLONGED-RELEASE TABLETS 0.4 MG | HANG LUNG TRADING (H.K.) CO |
| HK-68071 | TAMSULOSIN SANDOZ PROLONGED-RELEASE TABLETS 0.4MG | SANDOZ HONG KONG LIMITED |
| HK-61598 | APO-TAMSULOSIN CR TABLETS 0.4MG | HIND WING CO LTD |
| HK-55731 | HARNAL D TAB 0.2MG | ASTELLAS PHARMA HONG KONG COMPANY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測都只有模型分數，沒有臨床試驗或直接相關的文獻，證據等級為 L5。
- 對 Ambras 症候群找不到合理的藥理機轉，高分很可能是知識圖譜的鄰近效應。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料，確認是否有任何與毛囊或 TRPS1 路徑相關的機轉。
- 取得香港衞生署的仿單，補上警語與禁忌症，才能進入安全性篩選。
- 檢索 tamsulosin 與多毛症／毛髮疾病的直接研究（含前臨床研究）。若仍找不到，建議不再推進這個預測。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

