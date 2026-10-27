---
layout: default
title: Tropisetron
parent: 中證據等級 (L3-L4)
nav_order: 914
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Tropisetron：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L4）。原適應症：化療後噁心與嘔吐"
monitor_inn: "TROPISETRON"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Tropisetron
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

## Tropisetron：從化療引起的噁心嘔吐到偏頭痛
{: .text-alpha }

## 一句話總結

Tropisetron 是 5-HT3 受體拮抗劑，原本作為止吐藥，用於治療化療後的噁心與嘔吐。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
但目前**沒有臨床試驗**，僅有 **3 篇**機轉與藥理層面的文獻，屬於早期研究假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 化療後噁心與嘔吐（香港許可證未載明適應症，此為藥理資料庫所述的臨床用途） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Tropisetron 是 5-HT3 受體拮抗劑，同時也是 α7 菸鹼型受體的部分促效劑。藥理資料也顯示它會作用於 5-HT4 受體與甘胺酸受體（GLRA1、GLRA2、GLRB）。血清素訊號與偏頭痛的病理機轉有關，包括三叉神經血管系統的活化與腦膜血管擴張，因此阻斷 5-HT3 在機轉上有一定合理性。

目前的支持文獻主要是 5-HT3 拮抗劑的藥理學回顧，以及一篇與抗偏頭痛藥物比較的非臨床研究。另有貓的腦膜中動脈研究顯示 5-HT 可誘發血管擴張，支持血清素參與偏頭痛的機轉，但並未直接證明 tropisetron 的作用。

必須強調，**沒有任何臨床試驗**在偏頭痛患者中測試過 tropisetron。0.998 的 TxGNN 分數只是計算預測，不能取代臨床證據。

其他預測適應症（伴腦幹先兆的偏頭痛、偏頭痛易感性）屬於偏頭痛的亞型或相關表型，只能從一般血清素假說推論。至於萎縮性蠕蟲狀皮膚病 (atrophoderma vermiculata) 與眉部紅斑角化症 (ulerythema ophryogenesis)，並無合理的機轉依據，可能是知識圖譜的假象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7959407](https://pubmed.ncbi.nlm.nih.gov/7959407/) | 1994 | Review | Nihon Yakurigaku Zasshi | 回顧 5-HT3 受體拮抗劑（含 tropisetron）的藥理特性 |
| [8832453](https://pubmed.ncbi.nlm.nih.gov/8832453/) | 1996 | Review | J Clin Anesth | 回顧血清素與其受體在麻醉相關藥理中的角色 |
| [12924226](https://pubmed.ncbi.nlm.nih.gov/12924226/) | 2003 | Review | Eksp Klin Farmakol | 比較 tropoxin 與其他抗偏頭痛藥物對腦血管血清素反應的影響（非臨床） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61647 | SETROVEL SOLUTION FOR INJECTION 5MG/5ML | 注射液 | 許可證資料未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛適應症僅有計算預測與非臨床、藥理層面的間接證據，缺乏任何人體臨床資料，證據等級為 L4。
- 作用機轉與安全性資料（含仿單警語與禁忌）尚不完整，現階段不宜推進，可列為研究假說。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補齊完整的作用機轉資料（如 DrugBank）
- 針對偏頭痛進行 5-HT3 拮抗劑的文獻回顧，並評估是否有臨床前或小型探索性試驗的依據
- 評估給藥途徑的相容性（目前香港僅有注射劑型，偏頭痛慢性或預防用藥可能需要口服劑型）
- 暫不建議投入皮膚科預測適應症（萎縮性蠕蟲狀皮膚病、眉部紅斑角化症）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

