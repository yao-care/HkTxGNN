---
layout: default
title: Felbinac
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Felbinac：預測新適應症為Brachyolmia-Amelogenesis Imperfecta 症候群（證據等級 L5）。原適應症：骨關節炎、關節病變"
---

# Felbinac
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

# Felbinac：從骨關節炎到 Brachyolmia-Amelogenesis Imperfecta 症候群

## 一句話總結

Felbinac 是一種外用非類固醇消炎止痛藥（NSAID），原本用於骨關節炎與關節病變。
TxGNN 模型預測它可能對**Brachyolmia-Amelogenesis Imperfecta 症候群**有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測，證據等級為 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨關節炎、關節病變（香港許可證未載明適應症，此為知識圖譜資料） |
| 預測新適應症 | Brachyolmia-Amelogenesis Imperfecta 症候群 |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Felbinac 屬於外用 NSAID，一般認為是透過抑制環氧合酶（COX）發揮消炎止痛作用，用於肌肉骨骼疼痛與發炎。

Brachyolmia-Amelogenesis Imperfecta 症候群是罕見的遺傳性疾病，影響骨骼與牙釉質發育，與 LTBP3 等基因有關。COX 抑制對這類基因缺陷沒有已知的矯正作用。

這個高分預測較可能來自知識圖譜中與骨骼發育不良相關節點的網路鄰近性，而非生物學或臨床證據。即使有效，最多也只是緩解症狀，並非疾病修飾。

**其他預測適應症（同樣僅為模型預測，無試驗或文獻）：**

| 排名 | 疾病 | TxGNN 分數 | 合理性評估 |
|------|------|-----------|-----------|
| 2 | Acromesomelic dysplasia, Hunter-Thompson type | 99.99% | 由 GDF5 功能喪失變異造成，影響 BMP 訊號與軟骨生成；Felbinac 不作用於此路徑，至多緩解疼痛 |
| 3 | Myosclerosis | 99.99% | 肌肉纖維化與關節攣縮；僅有微弱間接可能（症狀緩解），無抗纖維化證據 |
| 4 | Brachyolmia | 99.99% | 遺傳性骨骼發育不良（如 PAPSS2、TRPV4 變異）；COX 抑制無法處理根本缺陷 |
| 5 | Pseudoachondroplasia | 99.99% | COMP 變異導致早發性骨關節炎；與 Felbinac 原適應症的關節疼痛有重疊，但僅為症狀緩解 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56207 | SUPER STRONG AMMELTZ FELBINA-ACE LIQUID | 未載明 | 未載明 |

廠商為 Kobayashi Pharmaceutical (Hong Kong) Company Limited，屬單一成分製劑，許可證有效。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 五個預測適應症都只有模型分數，沒有臨床試驗、文獻或明確的機轉支持。
- 這些疾病多為遺傳性骨骼或肌肉發育異常，NSAID 無法針對根本病因，最多只能緩解症狀。

**若要推進需要：**
- 補齊 Felbinac 的作用機轉資料（可查詢 DrugBank）。
- 取得香港衞生署仿單，確認警語、禁忌與核准適應症。
- 進行文獻與試驗的系統性檢索，確認是否有任何疾病相關證據。
- 若仍要探索，建議將目標限縮為「症狀緩解」（如 Pseudoachondroplasia 的繼發性關節疼痛），並評估外用途徑是否適用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

