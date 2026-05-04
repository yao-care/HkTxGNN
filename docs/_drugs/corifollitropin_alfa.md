---
layout: default
title: Corifollitropin Alfa
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Corifollitropin Alfa
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

# Corifollitropin alfa：從卵巢促排卵到胃十二指腸炎

## 一句話總結

Corifollitropin alfa 是一種長效促卵泡素（FSH）類似物，原本用於輔助生殖技術（ART）中的**受控卵巢刺激（COS）**。
TxGNN 模型在本次多適應症評估中，最高分預測為**胃十二指腸炎 (Gastroduodenitis)**（分數：99.65%）；
然而，10 個預測適應症均為 **L5 等級**，目前無任何臨床試驗或文獻支持，多數預測機轉合理性極低。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 受控卵巢刺激（Controlled Ovarian Stimulation, COS）－ ART 輔助生殖 |
| 預測最高分新適應症 | 胃十二指腸炎 (Gastroduodenitis) |
| TxGNN 預測分數（最高） | 99.65% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 待補充）。根據已知資訊，Corifollitropin alfa（商品名 Elonva，歐盟 EMA 核准）是一種長效重組 FSH 衍生物，由 FSHβ 亞基融合 hCG 的 C 端胜肽（CTP）而成，透過持續刺激**促卵泡素受體（FSHR）**，促進卵巢濾泡發育和雌二醇分泌，設計目的是在 COS 周期前 7 天取代每日注射 FSH，降低注射負擔。

**胃十二指腸炎**的病理核心是黏膜局部發炎，主因為幽門螺旋桿菌（*H. pylori*）感染、NSAIDs 使用或膽汁逆流。FSHR 的功能性表達主要侷限於**生殖器官**（卵巢顆粒細胞、睪丸 Sertoli 細胞），與胃腸黏膜保護路徑（前列腺素、黏液層合成、胃酸分泌）目前無已知直接關聯。

TxGNN 此項預測很可能源於知識圖譜中的**多步驟共病關聯**（如壓力→下視丘-腦垂體-性腺軸→腸道黏膜），而非直接藥理機轉。機轉合理性評估：**極低**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Corifollitropin alfa 目前**未在香港上市**，無任何藥物許可證記錄。

> 參考資訊：此藥在歐盟已獲 EMA 核准（商品名 Elonva，Merck/MSD），核准適應症為：**體重 > 60 kg 女性接受 ART 的受控卵巢刺激**。目前並無非生殖系統適應症的核准記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他預測適應症概覽（本次共 10 項，全部 L5）

本份為多適應症評估包（multi），以下列出全部預測及機轉合理性摘要，供優先排序參考：

| 排名 | 適應症 | TxGNN 分數 | 機轉合理性 | 方向備註 | 建議 |
|------|--------|-----------|-----------|---------|------|
| 1 | 胃十二指腸炎 (Gastroduodenitis) | 99.65% | **極低** | KG 多步驟共病效應 | Hold |
| 2 | 偏頭痛 (Migraine disorder) | 99.63% | **低至中** | FSH/雌激素軸 → 月經性偏頭痛觸發 | Research Question |
| 3 | 消化性潰瘍病 (Peptic ulcer disease) | 99.61% | **極低** | 胃腸酸相關疾病群 KG 鄰近效應 | Hold |
| 4 | 腦幹先兆偏頭痛 (Migraine with brainstem aura) | 99.59% | **低** | 與偏頭痛同群，荷爾蒙軸次優先 | Research Question |
| 5 | 雷諾氏病 (Raynaud disease) | 99.59% | **低至中** | 性別差異（F:M ≈ 9:1）、更年期惡化提示荷爾蒙調控 | Research Question |
| 6 | 肺動脈高壓 (Pulmonary hypertension) | 99.44% | **中**（⚠️ 方向存疑） | FSHR 於 PASMC 有功能性表達，FSH **可能促進** PASMC 增生，**方向可能有害** | Research Question |
| 7 | 脊椎側彎性心臟病 (Kyphoscoliotic heart disease) | 99.36% | **極低** | 純機械性病理，KG 經由「肺高壓」共病連結 | Hold |
| 8 | 偏頭痛遺傳易感性 (Migraine susceptibility) | 99.11% | **低** | 同偏頭痛群，建議合併評估，不單獨立項 | Research Question |
| 9 | 蟲蝕狀皮膚萎縮 (Atrophoderma vermiculata) | 98.81% | **極低** | 高度疑似語義偽陽性（皮膚 follicle ≠ 卵巢 follicle） | Hold |
| 10 | 消化性食道炎 (Peptic esophagitis) | 98.68% | **極低** | 胃腸酸相關疾病群，同 Rank 3 | Hold |

**機轉探索優先順序建議：**
1. 🔴 **肺動脈高壓（PAH）**：機轉可信度最高，但須優先確認**效果方向**（FSH 激動劑很可能惡化而非改善 PAH），屬高優先級安全性研究問題
2. 🟡 **偏頭痛/月經性偏頭痛**：FSH/雌激素軸有基礎生物學合理性，建議文獻探索（關鍵詞：FSH + migraine + estrogen + menstrual）
3. 🟡 **雷諾氏病**：性別差異和更年期相關性提供間接流行病學支持，但仍需機轉研究

---

## 結論與下一步

**決策：Hold**

**理由：**
本次 10 個預測適應症全部為 L5（僅模型預測），查無任何支持性臨床試驗或文獻；最高分預測（胃十二指腸炎）機轉合理性極低，高度懷疑為知識圖譜偽陽性。此外，Corifollitropin alfa 在香港尚未上市，安全性基礎資料（MOA、仿單警語）亦有待補充，目前不具備進入正式再利用評估的條件。

**若要推進需要：**
- **立即行動**：補充 DrugBank MOA 完整資訊及原廠仿單警語、禁忌症（解除 DG001、DG002 資料缺口）
- **機轉驗證（PAH 方向）**：搜尋 Huertas et al. 系列文獻（FSHR + pulmonary artery smooth muscle cell），**優先釐清 FSH 激動劑是否為有害方向**，避免潛在安全性風險
- **文獻探索（偏頭痛方向）**：關鍵詞 `FSH + migraine + estrogen + menstrual cycle` 進行初步掃描
- **雷諾氏病流行病學評估**：確認更年期 FSH 升高與症狀惡化之關聯文獻
- **監管可行性評估**：若未來有適應症立項，需規劃香港上市申請路徑及非 ART 情境下的劑量安全性設計
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

