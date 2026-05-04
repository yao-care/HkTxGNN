---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag：從免疫性血小板減少症到 Macrothrombocytopenia with Mitral Valve Insufficiency

---

## 一句話總結

Avatrombopag 是一種血小板生成素受體促效劑（TPO-RA），原本用於治療慢性免疫性血小板減少症（ITP）及慢性肝病相關血小板減少症。
TxGNN 模型預測它可能對**巨血小板減少症合併二尖瓣關閉不全（Macrothrombocytopenia with Mitral Valve Insufficiency）**有潛在療效，
然而目前**無任何臨床試驗**及**無任何文獻**支持這個具體適應症組合，整體證據等級為最低的 **L5**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 免疫性血小板減少症（ITP）／慢性肝病血小板減少症（香港未有上市記錄） |
| 預測新適應症（Rank 1） | Macrothrombocytopenia with Mitral Valve Insufficiency |
| TxGNN 預測分數 | 99.995% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前 Evidence Pack 中缺乏詳細的作用機轉（MOA）資料。根據已知資訊，Avatrombopag 屬於血小板生成素受體促效劑（TPO Receptor Agonist, TPO-RA）類別，其藥理機轉是與血小板生成素受體（c-Mpl）結合，促進巨核細胞增殖與分化，進而提升血小板數量。

Macrothrombocytopenia with Mitral Valve Insufficiency（巨血小板減少症合併二尖瓣關閉不全）是一種罕見的遺傳性症候群，典型代表為 MYH9 相關疾病（如 May-Hegglin 異常、Fechtner 症候群）。這類疾病的核心特徵是「血小板數量減少＋血小板體積異常增大（巨血小板）」，伴隨可能的心臟瓣膜異常。由於 Avatrombopag 的核心機轉是提升血小板「數量」，對於血小板數量不足的部分確實具有合理的機轉關聯性。

然而，有一個重要限制需要注意：MYH9 相關疾病的血小板減少源於巨核細胞分裂異常（血小板生成方式改變），而非 TPO 訊號不足，因此 TPO-RA 能否有效提升此類患者的血小板數量仍有不確定性。此外，即使血小板數量上升，每個巨血小板的功能缺陷（因 MYH9 突變導致的非肌肉肌球蛋白 IIA 功能喪失）依然存在，二尖瓣關閉不全亦與血小板機轉無直接關聯。

---

## 臨床試驗證據

目前無 Avatrombopag 用於 Macrothrombocytopenia with Mitral Valve Insufficiency 的相關臨床試驗登記。

---

## 文獻證據

目前無 Avatrombopag 用於 Macrothrombocytopenia with Mitral Valve Insufficiency 的相關文獻。

---

## 香港上市資訊

Avatrombopag 目前在香港尚未取得任何藥品許可證，無上市記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他預測適應症概覽

本次 TxGNN 共預測 10 個候選適應症，以下提供整體評估：

| 排名 | 疾病 | 機轉相關性 | 建議 |
|------|------|-----------|------|
| 1 | Macrothrombocytopenia with Mitral Valve Insufficiency | **強**（血小板減少症為核心靶標，但功能缺陷仍存在） | Research Question |
| 2 | Hereditary Thrombocytopenia with Normal Platelets | 中等（術語矛盾，效益不確定） | Research Question |
| 3 | Transient Neonatal Thrombocytopenia | 弱至中等（自限性，新生兒安全性完全未知） | Hold |
| 4 | Dense Granule Disease | **弱**（功能障礙而非數量不足，TPO-RA 無法修復 granule 分泌缺陷） | Hold |
| 5 | Amyotrophic Lateral Sclerosis（ALS） | **極弱**（神經退化疾病，無 TPO-RA 相關機轉） | Hold |
| 6 | Bilateral Parasagittal Parieto-Occipital Polymicrogyria | **無直接關聯**（腦部結構發育畸形） | Hold |
| 7 | Lower Motor Neuron Syndrome with Late-Adult Onset | **極弱**（類 ALS 亞型，同樣缺乏機轉基礎） | Hold |
| 8 | ALS, Susceptibility to | **極弱**（遺傳風險標記，無生物學基礎） | Hold |
| 9 | Mills Syndrome | **極弱**（罕見運動神經元疾病，ALS 變體） | Hold |
| 10 | Monomelic Amyotrophy（Hirayama 病） | **極弱**（脊髓局部缺血機轉，與 TPO-RA 完全無關） | Hold |

> **模式分析**：Rank 1–3 屬於血液學適應症，與 Avatrombopag 的 TPO-RA 機轉具有一定關聯性；Rank 4–10 中有多個神經科疾病，機轉關聯性極弱，可能反映知識圖譜中的遠端間接網絡連結，生物學合理性存疑。

---

## 結論與下一步

**決策：Hold**

**理由：**
所有 10 個預測適應症均為 L5 證據等級（純模型預測，零臨床試驗、零文獻支持），Avatrombopag 在香港亦尚未上市，缺乏監管基礎。雖然 Rank 1（Macrothrombocytopenia with Mitral Valve Insufficiency）在機轉上與 TPO-RA 有一定合理性，但該適應症屬於超罕見遺傳症候群，且 TPO-RA 在此疾病的效益存在根本的病理生理學不確定性。

**若要推進需要：**
- 補充 Avatrombopag 完整 MOA 資料（DrugBank API 查詢）
- 補充香港仿單或原廠 Full Prescribing Information，取得警語與禁忌症資料
- 針對 MYH9 相關疾病進行文獻回顧（Avatrombopag 或其他 TPO-RA 如 Eltrombopag 在遺傳性血小板減少症的既有研究）
- 評估 Eltrombopag（同類 TPO-RA）在類似適應症的文獻，作為 class effect 的間接參考
- 確認香港上市可行性（向衛生署提交新藥申請的可行性評估）

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過嚴格臨床驗證才能應用於臨床。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

