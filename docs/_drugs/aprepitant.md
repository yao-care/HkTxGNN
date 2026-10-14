---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant：從化療相關噁心嘔吐到腎因性抗利尿不適當症候群

## 一句話總結

Aprepitant 是一種 NK1 受體拮抗劑，在香港已有 7 張有效許可證。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (nephrogenic syndrome of inappropriate antidiuresis)** 有效，但目前**沒有任何臨床試驗或相關文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症 |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (nephrogenic syndrome of inappropriate antidiuresis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Aprepitant 屬於 NK1（Substance P）受體拮抗劑。NK1／Substance P 訊號與中樞神經系統的血管加壓素調節及水分平衡可能有關，因此在理論上存在連結。

不過，腎因性 SIADH 的成因是腎臟 V2 受體（AVPR2）功能獲得性突變，作用點在血管加壓素釋放的下游。中樞 NK1 拮抗不太可能矯正受體層級的缺陷，所以機轉上的合理性有限。高分預測目前只是模型輸出，沒有實證支持。

其他排名前 10 的預測（如多毛症、肺高壓、麻風、蛛網膜下腔出血等）同樣沒有臨床試驗支持，多數也缺乏合理機轉，可能是知識圖譜的關聯假象。肺高壓項下唯一連結的文獻（PMID 28261651）是 pazopanib 合併 cisplatin 的 Phase I 試驗，與 aprepitant 及肺高壓無關，應視為誤配，不提高證據等級。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52425 | EMEND CAP 80MG | — | 資料未載明 |
| HK-52424 | EMEND TRI-PACK CAP | — | 資料未載明 |
| HK-67479 | ATANTO TRI-PACK CAPSULES 125MG AND 80MG | — | 資料未載明 |
| HK-68461 | APREPITANT STADA CAPSULES 125MG AND 80MG | — | 資料未載明 |
| HK-67467 | EMEGON TRI-PACK CAPSULES 125MG AND 80MG | — | 資料未載明 |

（共 7 張有效許可證，以上列出 5 張。）

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：肝衰竭（liver failure）。此為知識圖譜中的藥物－疾病禁忌關聯，並非仿單文字。
- **藥物交互作用**：共查得 100 筆，其中較重要的包括：
  - 重度（Major）：Fentanyl、Alfentanil、Acalabrutinib
  - 中度（Moderate）：Paclitaxel、Abemaciclib、Nifedipine、Ibuprofen、Hydrocortisone、Fluvoxamine、Gefitinib 等

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或相關文獻，證據等級僅 L5。
- 腎因性 SIADH 的病因在腎臟 V2 受體，與 NK1 拮抗的作用位置不吻合。

**若要推進需要：**
- 取得 Aprepitant 完整的作用機轉資料，並釐清 NK1 訊號與 AVPR2 病理之間是否有可驗證的連結
- 進行前臨床或機轉研究，驗證 NK1 拮抗對水分平衡的作用
- 補齊香港仿單的核准適應症、警語與禁忌症
- 若後續出現其他支持證據，再重新評估排名較前的其他預測適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

